from django.urls import path, include
from .api.viewsets import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]