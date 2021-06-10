from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns =[
    path('', views.get_update_document),
    path('<str:id>', views.delete_document),
    path('id/<str:id>', views.get_by_id)
]