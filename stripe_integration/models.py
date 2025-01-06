from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=225)
    stripe_product_id = models.CharField(max_length=225)
    stripe_customer_id = models.CharField(max_length=225)
    stripe_checkout_id = models.CharField(max_length=225)
    currency = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=1)
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_name} --> {self.user.name}:: is paid --> {self.has_paid}"



