from django.urls import path 
from tobaccoauth import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
