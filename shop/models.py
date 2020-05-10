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

    def __str__(self):
        return self.name