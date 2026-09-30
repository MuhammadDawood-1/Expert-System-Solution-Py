"""
URL configuration for Dawood_project project.

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
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('showroom.urls')),
#     path('api-auth/',include('rest_framework.urls')),
#      # Login endpoint that returns access + refresh tokens.
#     path('api/token/', TokenObtainPairView.as_view()),
#     # Endpoint that creates a new access token using refresh token.
#     path('api/token/refresh/', TokenRefreshView.as_view()),
# ]
# """
# URL configuration for Dawood_project project.
# """

from django.contrib import admin
from django.urls import path, include

# JWT authentication views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # Your showroom API
    path('api/', include('showroom.urls')),

    # DRF browser login/logout
    path('api-auth/', include('rest_framework.urls')),

    # Login: username + password → access + refresh tokens
    path('api/token/', TokenObtainPairView.as_view()),

    # Refresh: refresh token → new access token
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

