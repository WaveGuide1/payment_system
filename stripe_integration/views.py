from django.shortcuts import render
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


def product_view(request):
    product_id = 'prod_RVxxVz8U51LR7H'
    product = stripe.Product.retrieve(product_id)
    prices = stripe.Price.list(product=product_id)
    price = prices['data'][0] if prices['data'] else None
    product_price = price.unit_amount / 100.0 if price else None
    return render(request, 'stripe/product.html', {'product': product, 'product_price': product_price})


