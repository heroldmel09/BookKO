from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Books

# Create your views here.
books = Books.objects.all()


def log_in(response):
    if response.method == "POST":
        username = response.POST.get("username")
        pass1 = response.POST.get("password")
        pass_con = response.POST.get("confirm-password")
        el = None
        if pass1 == pass_con:
            user = User.objects.create_user(username, el, pass1)
            user.save()
            messages.success(response, "you add in the database")
            return redirect(sing_in)
        else:
            return render(response, "home/BookKov2.html")

    return render(response, "login/UserLog.html")


def sing_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["password"]
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            return redirect(home_page2)
        else:
            return HttpResponse("invalid user")

    return render(request, "login/UserLog_copy.html")


def home_page2(request):
    return render(request, "home/BookKov2r.html", {"books": books})
