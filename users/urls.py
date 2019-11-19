from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/new', views.user_new, name='user_new'),
    #PROVEEDORES
    path('Lista_Proveedores', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #clientes
    path('Lista_Clientes', views.cliente_list, name='cliente_list'),
    path('Cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    path('Cliente/new', views.cliente_new, name='cliente_new'),
    path('Cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #productos
    path('Lista_Productos', views.produc_list, name='produc_list'),
    path('Producto/<int:pk>/', views.produc_detail, name='produc_detail'),
    path('Producto/new', views.produc_new, name='produc_new'),
    path('Producto/<int:pk>/edit/', views.produc_edit, name='produc_edit'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #creditos
    path('Lista_creditos', views.credito_list, name='credito_list'),
    path('credito/<int:pk>/', views.credito_detail, name='credito_detail'),
    path('credito/new', views.credito_new, name='credito_new'),
    path('credito/<int:pk>/edit/', views.credito_edit, name='credito_edit'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #ventas
    path('Lista_ventas', views.venta_list, name='venta_list'),
    path('venta/<int:pk>/', views.venta_detail, name='venta_detail'),
    path('venta/new', views.venta_new, name='venta_new'),
    path('venta/<int:pk>/edit/', views.venta_edit, name='venta_edit'),
]