"""storages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import main.views
from main.views import listener

admin.site.site_header = 'Панель администратора'
admin.site.index_title = 'Администрирование системы управления складами'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listener/', main.views.listener),
    path('', main.views.index),
    path('storage/', main.views.storage),
    path('owntemp/', main.views.ownTemp),
    path('refresh/', main.views.refreshData),
    path('keypress/', main.views.keyPress),
    path('chart/', main.views.chart),
]
