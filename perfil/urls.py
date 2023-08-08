from perfil import views
from django.urls import path

app_name = "perfil"

urlpatterns = [

path('', views.main, name='main'),
 path('/login', views.login, name='login'),
    path('/registar', views.registar, name='registar'),

]