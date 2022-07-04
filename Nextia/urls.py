from django.contrib import admin
from django.urls import path
from django.urls import include

#Necesarios para la autenticacion JWT

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
 
  
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Applications.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
