from django.urls import path, include
from . import views

app_name = 'cadastro'
urlpatterns = [

    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro')
]
