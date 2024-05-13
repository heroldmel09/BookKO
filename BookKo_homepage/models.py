from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField()
    genre = models.CharField(max_length=50)
    description = models.TextField()
    sub_genre = models.CharField(max_length=20, blank=True, null=True)
    image = models.TextField()
    page = models.CharField(max_length=20, blank=True, null=True)
    publish = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "books"

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=True, blank=True)
    last_name = models.CharField(max_length=150,null=True, blank=True)
    email = models.CharField(max_length=254)
    birthday=models.CharField(max_length=150,null=True, blank=True)
    gender=models.CharField(max_length=150,null=True, blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics/', blank=True, null=True ,default="profile_pics/nogame.jpg")
    id = models.AutoField(primary_key=True) 

    def __str__(self):
        return self.name


class YourOrder(models.Model):
    Customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    Date_order = models.DateTimeField(auto_now=True)
    Complete = models.BooleanField(default=False, null=True, blank=False)
    Transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_product_total(self):
        orderitem = self.orderitemcart_set.all()
        total = sum([items.get_total for items in orderitem])
        return total

    @property
    def get_product_total_item(self):
        orderitem = self.orderitemcart_set.all()
        total = sum([items.quantity for items in orderitem])
        return total


class OrderItemCart(models.Model):
    Product = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(
        YourOrder, on_delete=models.SET_NULL, null=True, blank=True
    )
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.Product.price * self.quantity
        return total


class Shipping_Address(models.Model):
    Customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True
    )
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    brgy = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=50, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    

class Books_Sale(models.Model):
   Books_onsale= models.OneToOneField(Books, null=True, blank=True, on_delete=models.CASCADE)
   sale_picture=models.ImageField(upload_to='profile_pics/', blank=True, null=True)

