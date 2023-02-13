from django.contrib import admin

from pedido.models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    model = Pedido

    list_display = [
        "id",
    ]
