from django.db import models

# Create your models here.

class Categoria(models.Model):
    CategoriaID = models.AutoField(primary_key=True)
    CategoriaNome = models.CharField(max_length=40)
    
    def __str__(self):
        return self.CategoriaNome

class Produto(models.Model):
    ProdutoID = models.AutoField(primary_key=True)
    ProdutoCodigo = models.UUIDField()
    ProdutoNome = models.CharField(max_length=60)
    ProdutoDescricao = models.CharField(max_length=500)
    ProdutoPreco = models.FloatField()
    ProdutoTamanho = models.CharField(max_length=10)
    Produtocategoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return self.ProdutoNome

class Cliente(models.Model):
    ClienteID = models.AutoField(primary_key=True)
    ClienteNome = models.CharField(500)
    ClienteIdade = models.PositiveSmallIntegerField()
    ClienteCpf = models.CharField(14)
    ClienteGenero = models.CharField(9)
    ClienteEmail = models.CharField(40)

    def __str__(self):
        return self.ClienteNome

class Pedido(models.Model):
    PedidoID = models.AutoField(primary_key=True)
    PedidoMetodoPagamento = models.CharField(15)
    PedidoStatus = models.CharField(60)
    PedidoData = models.DateField()
    PedidoEndereco = models.CharField(500)
    PedidoCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.PedidoID} - Cliente: {self.PedidoCliente.ClienteNome}"

class ItemPedido(models.Model):
    ItemPedidoID = models.AutoField(primary_key=True)
    ItemPedidoQuantidade = models.PositiveSmallIntegerField()
    ItemPedidoPrecoUnitario = models.FloatField()
    ItemPedidoPorProduto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens_pedidos')
    ItemPedidoPedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens_pedidos')

    def __str__(self):
        return f"ItemPedido {self.ItemPedidoID} - Produto: {self.ItemPedidoPorProduto.ProdutoNome}, Pedido: {self.ItemPedidoPedido.PedidoID}"
