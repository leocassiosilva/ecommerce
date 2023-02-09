from django.db import models

class Product(models.Model):

    name = models.CharField(
        'Nome', 
        max_length=100
    )
    score = models.PositiveIntegerField(
        'Score', 
        default=0
    )
    price = models.DecimalField(
        'Preço', 
        decimal_places=2, 
        max_digits=8
    )
    image = models.ImageField(
        'Imagem', 
        upload_to='products', 
        blank=True, 
        null=True
    )
    created = models.DateTimeField(
        'Criado em', 
        auto_now_add=True
    )
    modified = models.DateTimeField(
        'Modificado em', 
        auto_now=True
    )

    class Meta:
        app_label = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']
