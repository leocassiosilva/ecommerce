from django.db import models
from django.contrib.auth.models import User
from product.models import Product

class Cart(models.Model):

    user = models.OneToOneField(
        User, 
        verbose_name="Usuário", 
        related_name="cart",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    products = models.ManyToManyField(
        Product, 
        verbose_name="Produtos",
    )

    quantidade = models.PositiveIntegerField(
        verbose_name="Produtos", 
        default=1
    )

    class Meta:
        app_label = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'
        # ordering = ['product']