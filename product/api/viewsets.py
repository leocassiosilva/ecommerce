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

from product.api.serializers import ProductSerializer
from product.models import Product

class ProductViewSet(    
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
    }
    serializer_class = ProductSerializer

    #Listar todos os Products
    def get_queryset(self):
        return Product.objects.all()
    
    @action(detail=False, methods=["get"])
    def get_produtcs_filter(self, request, *args, **kwargs):
        filtro = request.GET.get('filtro', None)
        verificar_filtro = filtro == 'price' or filtro == 'score'

        if verificar_filtro: 
            products = Product.objects.all().order_by(filtro)
        else:
            products = Product.objects.all()


        if products.exists():

            data = list(products.values())
            return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
        else:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
            )