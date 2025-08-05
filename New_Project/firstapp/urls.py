from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.About),
    path('phone/', views.Phone),
]