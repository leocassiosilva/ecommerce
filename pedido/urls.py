from django.urls import path, include
from .api.viewsets import PedidoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'pedido', PedidoViewSet, basename='pedido')

urlpatterns = [
    path('', include(router.urls)),
]