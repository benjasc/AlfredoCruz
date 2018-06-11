from django import forms
from anuario.models import cliente, tipoInstrumento, proveedor, fondo, tipoInversion, tipoMovimiento

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ModalForm(forms.Form):#saldoInicial
    cliente = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= cliente.objects.values_list('id','nombre').order_by('id'))
    fecha   = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    tipoInstrumento = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}),choices=tipoInstrumento.objects.values_list('id','nombre').order_by('id'))
    proveedor = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= proveedor.objects.values_list('id','datos'))
    #fondo  = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}))
    monto = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={"class" : "form-control", 'placeholder': ''}))
    tipoInversion  = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= tipoInversion.objects.values_list('id','nombre').order_by('id'))

class ModalForm2(forms.Form):#movimiento
    cliente2 = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= cliente.objects.values_list('id','nombre').order_by('id'))
    fecha2   = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    tipoInstrumento2 = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}),choices=tipoInstrumento.objects.values_list('id','nombre').order_by('id'))
    proveedor2 = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= proveedor.objects.values_list('id','datos'))
    #fondo  = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}))
    monto2 = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={"class" : "form-control", 'placeholder': ''}))
    tipoInversion2  = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= tipoInversion.objects.values_list('id','nombre').order_by('id'))
    tipoMovimiento2 = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= tipoMovimiento.objects.values_list('id','nombre').filter(id__gte=2))

class Formimportarlista(forms.Form):
    archivo = forms.FileField(required=False)
    fixedincome = forms.FileField(required=False)
    assetallocation = forms.FileField(required=False)
    sectorexposure = forms.FileField(required=False)
    countryexposure = forms.FileField(required=False)
    
class formCliente(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    apellido_paterno = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    apellido_materno   = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))

class formPais(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    nombre_ingles = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))

class formDomicilio(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))

class formTipoInstrumento(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))

class formFrecuenciaDistribucion(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))

class formTipoInversion(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))

class formTipoMovimiento(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))

class formBindex(forms.Form):
    nombre = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))

class formAsignacionActivo(forms.Form):
    bono = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    efectivo = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    convertible = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    preferida = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    acciones = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    otra = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    fecha = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
