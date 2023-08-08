from carGest import views
from django.urls import path

app_name = "carGest"

urlpatterns = [

path('/carGest', views.carGest, name='carGest'),

]