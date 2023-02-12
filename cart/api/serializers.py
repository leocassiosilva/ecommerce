from rest_framework import serializers

from cart.models import Cart
from product.api.serializers import ProductSerializer



class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "user",
            "quantidade",
            "products"
        ]