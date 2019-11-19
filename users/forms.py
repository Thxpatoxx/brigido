from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import Proveedor,Cliente,Producto,Credito,Venta,Pedido

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = (
            'nombre', 
            'rut', 
            'persona_contacto', 
            'telefono', 
            'direccion', 
            'rubro', 
            )

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = (
            'rut', 
            'nombre',
            'apellido',
            'direccion',
            'telefono',
            'correo_electronico',
            )

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = (
            'proveedor', 
            'descripcion', 
            'precio',
            'marca',
            'existencia_actual',
            'cod_familia',
            'fecha_vencimiento',
            )
            
class CreditoForm(forms.ModelForm):
    class Meta:
        model = Credito
        fields = (
            'deudor', 
            'fecha',
            'monto_pago',
            'estado',
            'detalle_venta',
            )
            
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = (
            'cliente', 
            'fecha',
            'monto_pago',
            'detalle_venta',
            )

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = (
            'proveedor', 
            'fecha',
            'detalle_pedido',
            )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')