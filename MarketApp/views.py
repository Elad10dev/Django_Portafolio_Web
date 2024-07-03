from django.shortcuts import render, redirect,get_object_or_404
from .models import ItemDB, CartItemDB
# Create your views here.

def Inicio(request):   
    return render(request, 'inicio.html',)

def vitrina(request):
     items = ItemDB.objects.all()
     return render(request,
                       'market/vitrina.html',
                      {'items': items})

def carrito(request):
    item_cart = CartItemDB.objects.filter(user_id_id=request.user.id)
    for item in item_cart:
        item.subtotal = item.quantity * item.item_id.price
    
    # Calculamos el total a pagar
    total_amount = sum(item.subtotal for item in item_cart)
    
    context = {
        'item_cart': item_cart,
        'total_amount': total_amount,
    }
    return render (request,
                    'market/carrito.html',context
                    )

#agregar y eliminar articulos del carrito
def agregar_al_carrito(request, item_id):
        item = ItemDB.objects.get(item_id=item_id)
        cart_item, created = CartItemDB.objects.get_or_create(
        user_id=request.user,
        item_id=item,
        defaults={'quantity': 1},
        )
        if not created:
        # Si el artículo ya está en el carrito, incrementa la cantidad
            cart_item.quantity += 1
            cart_item.save()
        return redirect('carrito')  # Redirigir a la vitrina

def eliminar_del_carrito(request, item_id):
    cart_item = get_object_or_404(CartItemDB, user_id=request.user, id=item_id)
    cart_item.delete()
    return redirect('carrito')