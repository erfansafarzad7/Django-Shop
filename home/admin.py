from django.contrib import admin
from .models import Products,Category

admin.site.register(Category)
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    raw_id_fields = ('category', )
