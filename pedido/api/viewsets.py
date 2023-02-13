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
from pedido.api.serializers import PedidoSerializer
from pedido.models import Pedido
from rest_framework_simplejwt.authentication import JWTAuthentication

class PedidoViewSet(    
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    authentication_classes = [
        JWTAuthentication,
    ]

    serializer_class = PedidoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Pedido.objects.filter(user_id=self.request.user.id)
        return Pedido.objects.none()
    
