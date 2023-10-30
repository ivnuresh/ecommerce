from django.shortcuts import redirect, render
from shoppingapp.models import Product
from .models import Cart, CartItems
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()

    
    return cart


def add_cart(request,product_id):
  product=Product.objects.get(id=product_id)
  try:
     cart=Cart.objects.get(cart_id=_cart_id(request))
  except Cart.DoesNotExist:
     cart=Cart.objects.create(
        cart_id=_cart_id(request)
     ) 
     cart.save(),
  try:
     cart_item=CartItems.objects.get(product=product,cart=cart)
     cart_item.quantity +=1
     cart_item.save()

  except CartItems.DoesNotExist:
     cart_item=CartItems.objects.create(
        product=product,
        quantity=1,
        cart=cart
     )
     cart_item.save()

  return redirect('cartapp:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=None):
   
   try:
      cart=Cart.objects.get(cart_id=_cart_id(request))
      cart_items=CartItems.objects.filter(cart=cart,active=True)
      for cart_item in cart_items:
         total +=(cart_item.product.price * cart_item.quantity)
         counter +=cart_item.quantity
   except ObjectDoesNotExist:
      pass
   return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))   
def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItems.objects.get(product=product, cart=cart)
        cart_item.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('cartapp:cart_detail')


def remove_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItems.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('cartapp:cart_detail')


        
  