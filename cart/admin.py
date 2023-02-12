from django.contrib import admin

from cart.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    model = Cart

    list_display = [
        "id",
        "quantidade",

    ]