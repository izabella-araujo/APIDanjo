from django.urls import include, re_path
from EcoMmerce import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^produto$', views.produtoApi),
    re_path(r'^produto/([0-9]+)$', views.produtoApi),

    re_path(r'^categoria$', views.categoriaApi),
    re_path(r'^categoria/([0-9]+)$', views.categoriaApi),

    re_path(r'^cliente$', views.clienteApi),
    re_path(r'^cliente/([0-9]+)$', views.clienteApi),

    re_path(r'^pedido$', views.pedidoApi),
    re_path(r'^pedido/([0-9]+)$', views.pedidoApi),

    re_path(r'^itempedido$', views.itempedidoApi),
    re_path(r'^itempedido/([0-9]+)$', views.itempedidoApi)
]