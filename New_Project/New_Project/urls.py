from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', views.Content),
    path('', views.Home),
    path('firstapp/', include("firstapp.urls") ),
    path('index/', views.index),
    path('web/', include('secondapp.urls')),
]