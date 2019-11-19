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
]