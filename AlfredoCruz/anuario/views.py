from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,"login.html")

def index_user(request):
    return render(request,"index_user.html")

def index(request):
    return render(request,"index.html")
