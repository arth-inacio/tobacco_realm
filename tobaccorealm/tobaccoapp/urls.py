from django.urls import path 
from tobaccoapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
