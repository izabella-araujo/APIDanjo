from rest_framework import serializers
from EcoMmerce.models import Produto, Categoria, Cliente, Pedido, ItemPedido


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto
        fields=('ProdutoID', 'ProdutoCodigo', 'ProdutoNome', 'ProdutoDescricao', 'ProdutoPreco', 'ProdutoTamanho', 'Produtocategoria')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Categoria
        fields=('CategoriaID', 'CategoriaNome')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=('ClienteID', 'ClienteNome', 'ClienteIdade', 'ClienteCpf', 'ClienteGenero', 'ClienteEmail')

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pedido
        fields=('PedidoID', 'PedidoMetodoPagamento', 'PedidoStatus', 'PedidoData', 'PedidoEndereco', 'PedidoCliente')

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=ItemPedido
        fields=('ItemPedidoID', 'ItemPedidoQuantidade', 'ItemPedidoPrecoUnitario', 'ItemPedidoPorProduto', 'ItemPedidoPedido')