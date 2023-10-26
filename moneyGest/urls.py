"""
URL configuration for moneyGest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from carGest import views as carGest_views
from carteira import views as carteira_views
#from moneyGest import views as moneyGest_views
from perfil import views as perfil_views

urlpatterns = [
    path('admin/', admin.site.urls),    

                        #VIEWS DO PERFIL

    path('', perfil_views.main, name='main'),
    path('pagina_login/', perfil_views.pagina_login, name='pagina_login'),
    path('registar/', perfil_views.registar, name='registar'),
    path('do_login/', perfil_views.do_login, name='do_login'),

                        #//// END ////



                        #VIEWS DO CARGEST
                        
    path('carGest/', carGest_views.carGest, name='carGest'),
    path('addCarro/', carGest_views.addCarro, name='addCarro'),
    path('getCarro/', carGest_views.getCarro, name='getCarro'),
    path('addAbastecimento/', carGest_views.addAbastecimento, name='addAbastecimento'),
    
    path('abastecimentosJson/', carGest_views.abastecimentosJson, name='abastecimentosJson'),

    
                        #//// END ////



    



]
