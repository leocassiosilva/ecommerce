from django.urls import path, include
from .api.viewsets import CartViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
]