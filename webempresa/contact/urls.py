from django.urls import path
from . import views

urlpatterns = [
    #PATH APP CORE
    path('', views.contact, name='contact'),
]
 