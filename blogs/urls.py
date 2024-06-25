from django.urls import path
from . import views

urlpatterns = [
    path('', views.model_retrieval, name = 'home'),
    path('home/', views.model_retrieval, name = 'home'),

     
]
