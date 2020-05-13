from django.db import models
from django.contrib.auth.models import User
from django import forms




class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    sub_cat_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):

    p_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mrp = models.IntegerField()
    sp = models.IntegerField()
    desc = models.CharField(max_length=500)
    image = models.ImageField()
    cat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    available_quantity = models.IntegerField(default=100)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    p_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()

class Order(models.Model):
    o_id = models.AutoField(primary_key=True)
    u_id = models.ForeignKey(User, on_delete = models.SET_NULL, null=True)
    order_date = models.DateField()
    items = models.ManyToManyField(OrderItem)
    grand_total = models.IntegerField()
    fname = models.CharField(max_length=100, default='null')
    lname = models.CharField(max_length=100, default='null')
    contact = models.CharField(max_length=15,default='null')
    add1 = models.CharField(max_length=100,default='null')
    add2 = models.CharField(max_length=100, default='null')
    city = models.CharField(max_length=100, default='null')
    state = models.CharField(max_length=100, default='null')
    zipcode = models.CharField(max_length=100, default='null')
    
     
     





