from django.urls import path
from MarketApp.views import Inicio, vitrina
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('market/', Inicio,name='dashboard' ),
    path('market/vitrina', vitrina ,name='vitrina' ),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

