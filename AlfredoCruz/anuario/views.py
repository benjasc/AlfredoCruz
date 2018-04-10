from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from AlfredoCruz.forms import LoginForm
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
    return render(request,"index.html")
