from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product


# Create your views here.


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)

    context = {
        "cart": cart_obj,
    }
    return render(request, 'cart/home.html', context=context)


def cart_update(request):
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect("cart:home")

        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    # return redirect(product_obj.get_absolute_url())
    return redirect("cart:home")















