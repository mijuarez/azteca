from django.urls import path
from . import views

urlpatterns = [
    path('', views.prospects_index, name='prospects_index'),
    path('prospects_sign_in', views.prospects_sign_in, name='prospects_sign_in'),
    path('prospects_register/new', views.prospects_register, name='prospects_register'),
    path('prospects_list', views.prospects_list, name='prospects_list'),
]