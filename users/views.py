from django.shortcuts import render, get_object_or_404
from .models import Proveedor,Cliente,Producto,Credito,Venta
from .forms import ProveedorForm,CustomUserCreationForm,ClienteForm,ProductoForm,CreditoForm,VentaForm
from django.shortcuts import redirect


def index(request):
    return render(request, 'blog/index.html')
def user_new(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/user_edit.html', {'form': form})
#PROVEEDORES-----------------------------------------------------------
def post_list(request):
    posts = Proveedor.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ProveedorForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ProveedorForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
#---------------------------------------------------------------------------
#Clientes-----------------------------------------------------------
def cliente_list(request):
    posts = Cliente.objects.all()
    return render(request, 'cliente/cliente_list.html', {'posts': posts})
def cliente_detail(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/cliente_detail.html', {'post': post})
def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('cliente_detail', pk=post.pk)
    else:
        form = ClienteForm()
    return render(request, 'cliente/cliente_edit.html', {'form': form})
def cliente_edit(request, pk):
    post = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ClienteForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
#---------------------------------------------------------------------------
#Clientes-----------------------------------------------------------
def produc_list(request):
    posts = Producto.objects.all()
    return render(request, 'produc/produc_list.html', {'posts': posts})
def produc_detail(request, pk):
    post = get_object_or_404(Producto, pk=pk)
    return render(request, 'produc/produc_detail.html', {'post': post})
def produc_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('produc_detail', pk=post.pk)
    else:
        form = ProductoForm()
    return render(request, 'produc/produc_edit.html', {'form': form})
def produc_edit(request, pk):
    post = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ProductoForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})