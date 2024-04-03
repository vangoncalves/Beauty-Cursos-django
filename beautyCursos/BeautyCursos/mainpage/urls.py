from django.urls import path
from mainpage.views import home, cadastro, login, perfil, reservas_cursos

urlpatterns = [
    path('', home),
    path('cadastro/', cadastro),
    path('login/', login),
    path('perfil/', perfil),
    path('reservas_cursos/', reservas_cursos),
]