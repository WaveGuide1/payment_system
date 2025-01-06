from django.urls import path

from stripe_integration.views import *


urlpatterns = [
    path('', product_view, name='product'),
]