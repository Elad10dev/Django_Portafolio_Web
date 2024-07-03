from django.urls import path
from MarketApp.views import Inicio, vitrina, carrito, agregar_al_carrito, eliminar_del_carrito
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('market/', Inicio,name='dashboard' ),
    path('market/vitrina', vitrina ,name='vitrina' ),
    path('market/carrito', carrito ,name='carrito' ),
    #agregar y eliminar articulos del carrito
    path('market/add-to-cart/<int:item_id>/', agregar_al_carrito, name='agregar_al_carrito'),    
    path('market/remove-from-cart/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    
    
]
#con esto se ven las imagnes que se guardan en media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

