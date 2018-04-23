from django import forms
from anuario.models import cliente, tipoInstrumento, proveedor, fondo, tipoInversion

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class ModalForm(forms.Form):
    cliente = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= cliente.objects.values_list('nombre','nombre'))
    fecha   = forms.CharField(required=False, widget=forms.TextInput(attrs={"class" : "form-control", 'placeholder': ''}))
    tipoInstrumento = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= tipoInstrumento.objects.values_list('estructura_legal','estructura_legal'))
    proveedor = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= proveedor.objects.values_list('datos','datos'))
    fondo  = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= fondo.objects.values_list('nombre','nombre'))
    monto = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={"class" : "form-control", 'placeholder': ''}))
    tipoInversion  = forms.ChoiceField(required=False, widget=forms.Select(attrs={"class" : "form-control"}), choices= tipoInversion.objects.values_list('nombre','nombre'))
