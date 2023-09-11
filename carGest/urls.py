from carGest import views
from django.urls import path

app_name = "carGest"

urlpatterns = [

path('/carGest', views.carGest, name='carGest'),
#CRUD
path('/addAbastecimento', views.addAbastecimento, name='addAbastecimento'),
path('/addCarro', views.addCarro, name='addCarro'),

]