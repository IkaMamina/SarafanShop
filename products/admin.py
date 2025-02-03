from django.contrib import admin

from products.models import Category, SubCategory, Product

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)

