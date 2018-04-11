from django.shortcuts import render , redirect
from programmes.models import Programme
from .models import Cart
from orders.models import Order
from accounts.models import GuestEmail
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render (request, "cart/home.html", {"cart": cart_obj})


def cart_update(request):
    programme_id = request.POST.get('programme_id')
    if programme_id is not None:
        try:
            programme_obj = Programme.objects.get(id=programme_id)
        except Programme.DoesNotExist:
            print("Show message to user, programme is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if programme_obj in cart_obj.programmes.all():
            cart_obj.programmes.remove(programme_obj)
        else:
            cart_obj.programmes.add(programme_obj)
        request.session['cart_items'] = cart_obj.programmes.count()
    return redirect("cart:home")


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.programmes.count() == 0:
        return redirect("cart:home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    user = request.user
    billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get('guest_email_id')
    if user.is_authenticated:
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=user,email = user.email)

    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(email = guest_email_obj.email)
    else:
        pass
    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form
    }
    return render(request, "cart/checkout.html", context)
