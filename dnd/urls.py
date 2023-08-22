"""
URL configuration for dnd project.

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
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notas/', views.notas, name='notas'),
    path('', views.index, name='/'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('creator/', views.creator, name='creator'),
    path('characters/charlist', views.characterList, name='charlist'),
    path('base/error', views.error, name='error'),
    path('base/success', views.success, name='success'),
]
