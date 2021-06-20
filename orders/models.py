from django.db import models
from products.models import Product


class Order(models.Model):
    code = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=11)
    customer_email = models.EmailField()
    total_price = models.IntegerField(null=True)

    def __str__(self):
        return self.code


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(null=True)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return self.order.code
