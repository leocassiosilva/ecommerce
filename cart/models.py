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


    @property
    #A cada produto adicionado, deve-se somar R$ 10,00 ao frete.
    #Quando o valor dos produtos adicionados ao carrinho for igual ou superior a R$ 250,00, o frete é grátis.
    def calcular_frete(self):
        pass

    



    class Meta:
        app_label = 'cart'
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'
        # ordering = ['product']