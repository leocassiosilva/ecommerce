from django.contrib import admin

from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = [
        "id",
        "name",
        "price",
        "score",
    ]