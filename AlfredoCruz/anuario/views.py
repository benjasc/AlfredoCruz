from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from AlfredoCruz.forms import LoginForm, ModalForm
from django.contrib.auth import authenticate, login

# Create your views here.

def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    return HttpResponseRedirect( "perfil/")
                elif user.is_superuser:
                    return HttpResponseRedirect("index/")
                elif user.is_staff:
                    return HttpResponseRedirect("su/")
            else:
                return render(request,"login.html")
        else:
            return render(request,"login.html")
    else:
        return render(request,"login.html")
def perfil(request):
    return render(request,"index_user.html")

def index(request):
    form = ModalForm()
    contexto = {'form':form}
    return render(request,'index.html',contexto)

def SaldoInicial(request):
    return render(request,"SaldoInicial.html")

def tipoMovimiento(request):
    return render(request,"tipoMovimiento.html")

def tipoInversion(request):
    return render(request,"tipoInversion.html")

def Instrumento(request):
    return render(request,"Instrumento.html")
