from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet
from django.http import JsonResponse

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