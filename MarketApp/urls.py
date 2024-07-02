from django.urls import path
from MarketApp.views import Inicio

urlpatterns = [
    path('market/', Inicio,name='dashboard' ),
    
    
]

