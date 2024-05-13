from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from Log_inuser import views
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import register_forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import JsonResponse
import json
import random
from django.db.models import Q
from django.core.files import File
from django.conf import settings





# Create your views here.
genrelist = ["Horror", "Fantasy", "History", "Mystery Detective", "Romance","Adventure","Fiction and Literature","YOUNG READERS"]
books = Books.objects.all()


def index(request):
    return HttpResponse("Log in sucssesfuly")


def home_page(request):
    result1, result2, result3 = random.sample(genrelist, 3)
    genre1 = Books.objects.filter(genre=result1,).all()
    genre2 = Books.objects.filter(genre=result2,).all()
    genre3 = Books.objects.filter(genre=result3,).all()
    sale_pic = Books_Sale.objects.all()
    if request.method == "POST":
        regis = register_forms(request.POST)
        if "register" in request.POST:
            if regis.is_valid():
                pass1 = regis.cleaned_data.get("password1")
                pass2 = regis.cleaned_data.get("password2")
                email = regis.cleaned_data.get('email')
                username= regis.cleaned_data.get('username')

                if pass1 == pass2:
                    user = User.objects.create_user(username=username, email=email, password=pass1)
                    customer=Customer.objects.create(user=user,name=username,email=email)
                    customer.save()
                    messages.success(request, "you add in the database")
                    return HttpResponse("you add in the database")
                else:
                    messages.success(request, "you did not add in the database")
                    return HttpResponse("you did not add in the database")

        elif "login" in request.POST:
            username1 = request.POST["user"]
            pass1 = request.POST["password"]
            user = authenticate(username=username1, password=pass1)

            if user is not None:
                login(request, user)
                return redirect(home_page2)
            else:
                return HttpResponse("invalid user")
    else:
        regis = register_forms()
    return render(request, "home/BookKov2.html", {"books": genre1,"genrename":result1,"books1": genre2,"genrename1":result2,"books2": genre3,"genrename2":result3, "forms": regis,"sale_pic":sale_pic,"Gsearh":genrelist})


def home_page2(request):
    result1, result2, result3 = random.sample(genrelist, 3)
    genre1 = Books.objects.filter(genre=result1,).all()
    genre2 = Books.objects.filter(genre=result2,).all()
    genre3 = Books.objects.filter(genre=result3,).all()
    sale_pic = Books_Sale.objects.all()
    return render(request, "home/BookKov2Log.html", {"books": genre1,"genrename":result1,"books1": genre2,"genrename1":result2,"books2": genre3,"genrename2":result3,"sale_pic":sale_pic,"Gsearh":genrelist})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = YourOrder.objects.get_or_create(
            Customer=customer, Complete=False
        )
        item = order.orderitemcart_set.all()
    else:
        item = []

    return render(request, "home/Booko_cart.html", {"items": item, "order": order,"Gsearh":genrelist})


def user_settings(request):
    try:
        user_info = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        user_info = None

    if request.method == "POST":
        if "info_update" in request.POST:
            if user_info is None:
                user_info = Customer(user=request.user)

            if request.POST.get("info_name", ""):
                user_info.name=request.POST.get("info_name", "")
            if request.POST.get("info_email", ""):
                user_info.email=request.POST.get("info_email", "")
            if request.POST.get("info_birth", ""):
                user_info.birthday=request.POST.get("info_birth", "")
            if request.POST.get("info_gender", ""):
                user_info.gender=request.POST.get("info_gender", "")

            user_info.save(update_fields=["name", "email", "birthday", "gender"])

        if "update_photo" in request.POST:
            if user_info is None:
                user_info = Customer(user=request.user)

            if request.FILES.get("info_profile_pic"):
                # Open the image file
                with request.FILES["info_profile_pic"] as f:
                    # Create a new Django File object using the image file
                    file_obj = File(f)

                    # Set the profile_pic attribute of the user object to the new File object
                    user_info.profile_pic = file_obj
                    
                    # Save the user object
                    user_info.save(update_fields=["profile_pic"])

        return render(request, "home/usersettings.html", {"user_info":user_info,"Gsearh":genrelist})

    return render(request, "home/usersettings.html", {"user_info":user_info,"Gsearh":genrelist})

def log_out(request):
    logout(request)
    return redirect(home_page)


def updatecart(request):
    data = json.loads(request.body)
    productid = data["productID"]
    action = data["action"]
    print(productid, "and", action)
    customer = request.user.customer
    product = Books.objects.get(id=productid)
    order, created = YourOrder.objects.get_or_create(Customer=customer, Complete=False)
    orderitemcart, created = OrderItemCart.objects.get_or_create(
        order=order, Product=product
    )

    if action == "add":
        orderitemcart.quantity = orderitemcart.quantity + 1
    elif action == "remove":
        orderitemcart.quantity = orderitemcart.quantity - 1

    orderitemcart.save()

    if orderitemcart.quantity <= 0:
        orderitemcart.delete()

    return JsonResponse("item was add in db", safe=False)


def book_ID(request, bookID):
    print(bookID) 
    genre= get_object_or_404(books, pk=bookID)
    genreid = Books.objects.filter(genre=genre.genre).all()
    return render(
        request, "home/Book_id.html", {"book_iD": get_object_or_404(books, pk=bookID),"genreid":genreid,"Gsearh":genrelist}
    )


def search_book(request):
    booksearch=request.GET.get('booksearch','')
    Book_seach=Books.objects.filter(Q(name__icontains=booksearch) |Q (author__icontains=booksearch))
    print(booksearch)
    if len(Book_seach)==1:
        for obj in Book_seach:
           return book_ID(request,obj.id)
    else:
        return render(request, "home/search_page.html",{"search":booksearch ,"search_result":Book_seach,"Gsearh":genrelist})

def genre_search(request, genreID):
    if genreID=="Mystery Detective":
        genreID="Mystery/Detective"
        genreid = Books.objects.filter(genre=genreID).all()
    else:
       genreid = Books.objects.filter(genre=genreID).all()     
    return render(request, "home/search_page.html",{"genre":genreid,"genrename":genreID,"Gsearh":genrelist})