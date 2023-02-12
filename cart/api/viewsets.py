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
from cart.models import Cart, CartItem
from django.db.models import Sum, Count
from product.api.serializers import ProductSerializer
from product.models import Product

class CartViewSet(    
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
    }
    serializer_class = CartSerializer

    @action(detail=True, methods=["get"])
    def add_cart_itens (self, request, *args, **kwargs):
        id_produto = request.GET.get('id', None)
        quantidade = request.GET.get('quantidade', None)

        id_cart = int(kwargs['pk'])
        try: 
            #consulta um Cart 
            cart = Cart.objects.filter(pk=id_cart)
            for carrinho in cart:
                cart_item_produto = carrinho.cart_itens.filter(products_id=id_produto)
            
            verificar_quantidade = quantidade == None or quantidade == 1
            if verificar_quantidade:
                quantidade = 1

            if cart_item_produto.exists():
                for cart_produto in cart_item_produto:  
                    # cart_produto.quantidade = (cart_produto.quantidade + int(quantidade))
                    cart_item_produto.update(quantidade=cart_produto.quantidade + int(quantidade))
            else: 
                produto = Product.objects.get(pk=id_produto)
                carrinhoItem = CartItem.objects.create(products=produto, quantidade=quantidade)
                for carrinho in cart:            
                    carrinho.cart_itens.add(carrinhoItem)
            
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("Errro {e}")
            return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=["get"])
    def remove_cart_itens (self, request, *args, **kwargs):
        id_produto = request.GET.get('id', None)

        id_cart = int(kwargs['pk'])
        try: 
            #consulta um Cart 
            cart = Cart.objects.filter(pk=id_cart)
            for carrinho in cart:
                cart_item_produto = carrinho.cart_itens.filter(products_id=id_produto)
            
            if cart_item_produto.exists():
                for item in cart_item_produto:
                    if item.quantidade == 1:
                        cart_item_produto.delete()
                    else:
                        cart_item_produto.update(quantidade=item.quantidade - 1)
            
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("Errro {e}")
            return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=["get"])
    def cart_itens (self, request, *args, **kwargs):
        id_cart = int(kwargs['pk'])
        try: 
            cart = Cart.objects.get(pk=id_cart)
            carts = cart.cart_itens.all()
            valor_total = 0
            quantidade_produtos = 0
            frete = 0
            produtos = []  

            if carts.exists():
                for item in carts: 
                    quantidade_produtos += item.quantidade
                    valor_total += (item.products.price * item.quantidade)
                    produtos.append(item.products.id)

                if valor_total < 250.00:
                    frete = quantidade_produtos * 10 

                prod = list(Product.objects.filter(pk__in=produtos).values())


                data = {
                    'produtos': prod,
                    'Frete':frete,
                    'Valor Total': valor_total + frete,
                }
      
                return JsonResponse(data, safe=False,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print("Errro {e}")

            return Response(
                    {"message": "Errro {e}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

class CartItemViewSet(    
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):

    permission_classes_by_action = {
        "create": [permissions.IsAuthenticated],
    }
    serializer_class = CartSerializer

