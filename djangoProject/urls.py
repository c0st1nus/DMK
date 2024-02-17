"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import DMK.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DMK.views.home, name='home'),
    path('test/', DMK.views.test, name='new_page'),
    path('comingSoon/', DMK.views.comingSoon, name='ComingSoon'),
    path('physics/', DMK.views.physics, name='Physics'),
    path('constructor/', DMK.views.constructor, name='Constructor'),
    path('add-item/', DMK.views.add_item, name='add_item'),
]
