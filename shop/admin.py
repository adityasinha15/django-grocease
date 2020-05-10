from django.contrib import admin
from .models import Category, Product, SubCategory

class Prod(admin.ModelAdmin):
    readonly_fields = ('p_id',)

class Cat(admin.ModelAdmin):
    readonly_fields = ('cat_id',)

class Scat(admin.ModelAdmin):
    readonly_fields = ('sub_cat_id',)

admin.site.register(Product, Prod)

admin.site.register(Category, Cat)
admin.site.register(SubCategory, Scat)

