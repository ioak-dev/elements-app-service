"""elements URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url

from . import views

urlpatterns = [
    path('task/<str:task_id>/status', views.get_status),
    path('task/<str:task_id>/result', views.get_result),
    path('admin/<str:space_id>/', admin.site.urls),
    path('auth/', include('app.auth.urls')),
    path('space/', include('app.space.urls')),
    path('user/<str:space_id>/', include('app.user.urls')),
    path('site/', include('app.site.urls')),
    path('document/', include('app.document.urls')),
    path('role/<str:space_id>/', include('app.role.urls')),
]
