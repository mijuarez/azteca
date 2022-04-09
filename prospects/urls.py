from django.urls import path
from . import views

urlpatterns = [
    path('', views.prospects_list, name='prospects_list'),
]