from rest_framework import serializers
from cart.api.serializers import CartSerializer
from pedido.models import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    # cart_itens = CartSerializer(many=True, read_only=False)

    class Meta:
        model = Pedido
        fields = [
            "id",
            "user",
            "cart_itens"
        ]
    #metodo criar um Pedido
    def create(self, validated_data):
        return Pedido.objects.create(**validated_data)
