from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('users/', include('visit.urls')),
   path('users/', include('django.contrib.auth.urls')),

   path('admin/', admin.site.urls),
   path('', views.home, name='home')
]
