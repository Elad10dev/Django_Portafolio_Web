from django.urls import path
from MainApp.views import Index 

urlpatterns = [
    path('', Index, name='index' ),
    
    
    
]


