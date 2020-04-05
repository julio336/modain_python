from django.contrib import admin
from .models import Product, Comment, ImageProduct, ShoppingCart

@admin.register(Product, Comment, ImageProduct, ShoppingCart)
class AuthorAdmin(admin.ModelAdmin):
    pass