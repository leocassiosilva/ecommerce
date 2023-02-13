from django.db import models
from django.contrib.auth.models import User

from cart.models import CartItem

class Pedido(models.Model):

    STATUS_CHOICES = (
        (0, 'Pedido Efetuado'),
        (1, 'Pedido Enviado'),
        (2, 'Pedido Cancelado'),
        (3, 'Pedido Finalizado')
    )

    user = models.ForeignKey(
        User, 
        verbose_name="Usuário", 
        related_name="pedido",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    status = models.IntegerField(
        'Situação', 
        choices=STATUS_CHOICES, 
        default=0, 
        blank=True
    )

    cart_itens = models.ManyToManyField(
        CartItem, 
        verbose_name="CartItems",
        blank=True,
    )

    def __str__(self):
        return "{}".format(self.status)

    class Meta:
        app_label = 'pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedido'
        # ordering = ['name']
