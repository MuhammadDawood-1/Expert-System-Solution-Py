from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_my_form, name='property_form'),
]