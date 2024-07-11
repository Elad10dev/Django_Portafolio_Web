from django.shortcuts import render, redirect,get_object_or_404
from .models import ItemDB, CartItemDB
from .form import LoginForm, UserRegistrationForm
#para iniciar sesion y logingrequired
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
#verificacion de informacion de usuarios correcta
from    django.http import HttpResponse
# Create your views here.

def Inicio(request):   
    return render(request, 'inicio.html',)


def vitrina(request):
     items = ItemDB.objects.all()
     return render(request,
                       'market/vitrina.html',
                      {'items': items})

@login_required
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
@login_required
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

@login_required
def eliminar_del_carrito(request, item_id):
    cart_item = get_object_or_404(CartItemDB, user_id=request.user, id=item_id)
    cart_item.delete()
    return redirect('carrito')

#registro de usuarios agregar carpeta form y formularios de django
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 
                      'account/register.html',
                      {'user_form': user_form})

#inicio de sesio agregar contrib de django ara login y authenticated
def user_login(request):
    if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                 cd = form.cleaned_data
                 user = authenticate(request,
                                     username = cd['username'],
                                     password = cd['password'])
            if user is not None:
                 if user.is_active:
                    login(request, user)
                    return HttpResponse ('Usuario autenticado')
                 else:
                      return HttpResponse('Usuario inactivo')
            else:
                 return HttpResponse('Informacion incorrecta')
    else:
         form = LoginForm()
         return render(request, 'account/login.html',{'form':form})