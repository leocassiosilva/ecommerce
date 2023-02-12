from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework import permissions, status
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse
from rest_framework.decorators import action
from cart.api.serializers import CartSerializer
from cart.models import Cart

from product.api.serializers import ProductSerializer
from product.models import Product

class CartViewSet(    
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
    }
    serializer_class = CartSerializer


    @action(detail=True, methods=["get"])
    def remover_product(self, request, *args, **kwargs):
        id_produto = request.GET.get('id', None)
        id_cart = int(kwargs['pk'])
        if id_produto is not None:
            try: 
                cart = Cart.objects.get(pk=id_cart)

                cart_product = cart.products.filter(pk=1)

                if cart_product.exists():
                    cart_product.delete()
                    return Response(
                            {"message": "Produto removido com sucesso!!"},
                            status=status.HTTP_200_OK
                        )
                
                return Response(status=status.HTTP_204_NO_CONTENT)
                
            except Exception as e:
                print("Errro {e}")

        return Response(
                {"message": "O id do produto não é valido existe."},
                status=status.HTTP_400_BAD_REQUEST,
            )