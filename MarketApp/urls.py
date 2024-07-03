from django.urls import path
from MarketApp.views import Inicio, vitrina, carrito, agregar_al_carrito, eliminar_del_carrito, register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views#Para el inicio de sesion!

urlpatterns = [
    path('market/', Inicio,name='dashboard' ),
    path('market/vitrina', vitrina ,name='vitrina' ),
    path('market/carrito', carrito ,name='carrito' ),
    #agregar y eliminar articulos del carrito
    path('market/add-to-cart/<int:item_id>/', agregar_al_carrito, name='agregar_al_carrito'),    
    path('market/remove-from-cart/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    #agregamos la ruta para registro de usuarios
    path('market/register/', register, name='register'),
    #agregar el inicio de sesion
    path('market/login/', auth_views.LoginView.as_view(), name='login'),
    #cerrar sesion y cambiar contraseña
    path('market/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('market/password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('market/password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    
]
#con esto se ven las imagnes que se guardan en media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

