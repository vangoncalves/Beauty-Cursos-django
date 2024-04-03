from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')

def perfil(request):
    return render(request, 'perfil.html')

def reservas_cursos(request):
    return render(request, 'reservas_cursos.html')