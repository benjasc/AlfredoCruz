from django import forms
from anuario.models import cliente, tipoInstrumento, proveedor, fondo, tipoInversion, tipoMovimiento

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ModalForm(forms.Form):
    cliente = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= cliente.objects.values_list('id','nombre').order_by('id'))
    fecha   = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    tipoInstrumento = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}),choices=tipoInstrumento.objects.values_list('id','estado_distribucion').order_by('id'))
    proveedor = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= proveedor.objects.values_list('id','datos'))
    #fondo  = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}))
    monto = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={"class" : "form-control", 'placeholder': ''}))
    tipoInversion  = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= tipoInversion.objects.values_list('id','nombre').order_by('id'))
    tipoMovimiento = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= tipoMovimiento.objects.values_list('id','nombre').filter(id__gte=2))
