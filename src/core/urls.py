"""
URL configuration for core project.

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
from django.urls import path
from .views import index
from django.contrib import admin
from django.urls import path
from .views import cadastro_candidato
from .views import principal_candidato
from .views import cadastrar
from .views import login_usuario
from .views import login_admin
from .views import cadastro_admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('cadastro_candidato/',cadastro_candidato),
    path("principal_candidato/", principal_candidato), #chamada da view para mostrar o template principal_candidato.html
    #path para o perfil do candidato
    path("cadastrar/", cadastrar),
    path("login_usuario/", login_usuario),
    path("login_admin/", login_admin),
    path("cadastro_admin/", cadastro_admin),
]
