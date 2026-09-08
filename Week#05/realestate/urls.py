"""
URL configuration for realestate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path,include 
# Yahan 'forms' ki jagah apni us App ka sahi naam likhein jahan forms.py aur views.py hain


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mse/', include('mse.urls')),
    # Aap ke views.py mein function ka naam 'show_my_form' hai, isliye hum yahan wohi likhenge
    # path('', views.show_my_form, name='property_form'),
]