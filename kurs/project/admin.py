from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Changes)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'product_id')


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_path')
