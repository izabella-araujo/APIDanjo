from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EcoMmerce.models import Produto, Categoria, Cliente, Pedido, ItemPedido
from EcoMmerce.serializers import ProdutoSerializer, CategoriaSerializer, ClienteSerializer, PedidoSerializer, ItemPedidoSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def produtoApi(request,id=0):
    if request.method=='GET':
        produtos = Produto.objects.all()
        produtos_serializer=ProdutoSerializer(produtos,many=True)
        return JsonResponse(produtos_serializer.data,safe=False)
    elif request.method=='POST':
        produto_data=JSONParser().parse(request)
        produtos_serializer=ProdutoSerializer(data=produto_data)
        if produtos_serializer.is_valid():
            produtos_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar",safe=False)
    elif request.method=='PUT':
        produto_data=JSONParser().parse(request)
        produto=Produto.objects.get(ProdutoID=produto_data['ProdutoID'])
        produtos_serializer=ProdutoSerializer(produto,data=produto_data)
        if produtos_serializer.is_valid():
            produtos_serializer.save()
            return JsonResponse("Atualizado com sucesso",safe=False)
        return JsonResponse("Falha ao atualizar")
    elif request.method=='DELETE':
        produto=Produto.objects.get(ProdutoID=id)
        produto.delete()
        return JsonResponse("Deletado com sucesso",safe=False)
    

@csrf_exempt
def categoriaApi(request,id=0):
    if request.method=='GET':
        categoria = Categoria.objects.all()
        categoria_serializer=CategoriaSerializer(categoria,many=True)
        return JsonResponse(categoria_serializer.data,safe=False)
    elif request.method=='POST':
        categoria_data=JSONParser().parse(request)
        categoria_serializer=CategoriaSerializer(data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar",safe=False)
    elif request.method=='PUT':
        categoria_data=JSONParser().parse(request)
        categoria=Categoria.objects.get(CategoriaID=categoria_data['CategoriaID'])
        categoria_serializer=CategoriaSerializer(categoria,data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return JsonResponse("Atualizado com sucesso",safe=False)
        return JsonResponse("Falha ao atualizar")
    elif request.method=='DELETE':
        categoria=Categoria.objects.get(CategoriaID=id)
        categoria.delete()
        return JsonResponse("Deletado com sucesso",safe=False)
    

@csrf_exempt
def clienteApi(request,id=0):
    if request.method=='GET':
        clientes = Cliente.objects.all()
        clientes_serializer=ClienteSerializer(clientes,many=True)
        return JsonResponse(clientes_serializer.data,safe=False)
    elif request.method=='POST':
        cliente_data=JSONParser().parse(request)
        clientes_serializer=ClienteSerializer(data=cliente_data)
        if clientes_serializer.is_valid():
            clientes_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar",safe=False)
    elif request.method=='PUT':
        cliente_data=JSONParser().parse(request)
        cliente=Cliente.objects.get(ClienteID=cliente_data['ClienteID'])
        clientes_serializer=ClienteSerializer(cliente,data=cliente_data)
        if clientes_serializer.is_valid():
            clientes_serializer.save()
            return JsonResponse("Atualizado com sucesso",safe=False)
        return JsonResponse("Falha ao atualizar")
    elif request.method=='DELETE':
        cliente=Cliente.objects.get(ClienteID=id)
        cliente.delete()
        return JsonResponse("Deletado com sucesso",safe=False)
    

@csrf_exempt
def pedidoApi(request,id=0):
    if request.method=='GET':
        pedidos = Pedido.objects.all()
        pedidos_serializer=PedidoSerializer(pedidos,many=True)
        return JsonResponse(pedidos_serializer.data,safe=False)
    elif request.method=='POST':
        pedido_data=JSONParser().parse(request)
        pedidos_serializer=PedidoSerializer(data=pedido_data)
        if pedidos_serializer.is_valid():
            pedidos_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar",safe=False)
    elif request.method=='PUT':
        pedido_data=JSONParser().parse(request)
        pedido=Pedido.objects.get(PedidoID=pedido_data['PedidoID'])
        pedidos_serializer=PedidoSerializer(pedido,data=pedido_data)
        if pedidos_serializer.is_valid():
            pedidos_serializer.save()
            return JsonResponse("Atualizado com sucesso",safe=False)
        return JsonResponse("Falha ao atualizar")
    elif request.method=='DELETE':
        pedido=Pedido.objects.get(PedidoID=id)
        pedido.delete()
        return JsonResponse("Deletado com sucesso",safe=False)
    

@csrf_exempt
def itempedidoApi(request,id=0):
    if request.method=='GET':
        itenspedidos = ItemPedido.objects.all()
        itenspedidos_serializer=ItemPedidoSerializer(itenspedidos,many=True)
        return JsonResponse(itenspedidos_serializer.data,safe=False)
    elif request.method=='POST':
        itempedido_data=JSONParser().parse(request)
        itenspedidos_serializer=ItemPedidoSerializer(data=itempedido_data)
        if itenspedidos_serializer.is_valid():
            itenspedidos_serializer.save()
            return JsonResponse("Adicionado com sucesso",safe=False)
        return JsonResponse("Falha ao adicionar",safe=False)
    elif request.method=='PUT':
        itempedido_data=JSONParser().parse(request)
        itempedido=ItemPedido.objects.get(ItemPedidoID=itempedido_data['ItemPedidoID'])
        itenspedidos_serializer=ItemPedidoSerializer(itempedido,data=itempedido_data)
        if itenspedidos_serializer.is_valid():
            itenspedidos_serializer.save()
            return JsonResponse("Atualizado com sucesso",safe=False)
        return JsonResponse("Falha ao atualizar")
    elif request.method=='DELETE':
        itempedido=ItemPedido.objects.get(ItemPedidoID=id)
        itempedido.delete()
        return JsonResponse("Deletado com sucesso",safe=False)
    

