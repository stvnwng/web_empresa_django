from django.urls import path
from . import views

urlpatterns = [
    #PATH APP SERVICES
    path('', views.services, name='services'),
]
