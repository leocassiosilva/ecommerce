from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "score",
        ]
    #metodo criar um produto
    def create(self, validated_data):
        return Product.objects.create(**validated_data)