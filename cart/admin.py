from django.contrib import admin

from cart.models import Cart, CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart

    list_display = [
        "id",
    ]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    model = Cart

    list_display = [
        "id",
    ]