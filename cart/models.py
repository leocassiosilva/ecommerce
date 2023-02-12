from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class CartItem(models.Model):

    products = models.ForeignKey(
        Product, 
        verbose_name="Produtos",
        on_delete=models.CASCADE
    )

    quantidade = models.PositiveIntegerField(
        verbose_name="Quantidade", 
        default=1
    )

    def __str__(self):
        return "{}".format(self.products)

    class Meta:
        app_label = 'cart'
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Item'


class Cart(models.Model):

    user = models.OneToOneField(
        User, 
        verbose_name="Usuário", 
        related_name="cart",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    cart_itens = models.ManyToManyField(
        CartItem, 
        verbose_name="CartItems",
        blank=True,

    )

    def __str__(self):
        return "{}".format(self.user)


    class Meta:
        app_label = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'


