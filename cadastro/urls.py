from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.contato_view, name='home'),
]
