from rest_framework import serializers

from cart.models import Cart, CartItem
from product.api.serializers import ProductSerializer



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "user",
            "cart_itens"
        ]

    
class CartItemSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=False)
    class Meta:
        model = CartItem
        fields = [
            "id",
            "products",
            "quantidade"

        ]