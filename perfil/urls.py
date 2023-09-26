from perfil import views
from django.urls import path

app_name = "perfil"

urlpatterns = [

path('', views.main, name='main'),
path('/pagina_login', views.pagina_login, name='pagina_login'),
path('/do_login', views.do_login, name='do_login'),
path('/registar', views.registar, name='registar'),

]