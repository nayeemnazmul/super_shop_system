import os

import qrcode
from num2words import num2words

from django.db import models
from django.conf import settings

from products.models import Product


class Order(models.Model):
    code = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=11)
    customer_email = models.EmailField()
    total_price = models.IntegerField(null=True)

    def __str__(self):
        return self.code

    @property
    def total_price_in_word(self):
        return num2words(self.total_price)

    @property
    def customer_info_in_qrcode_path(self):
        qrcode_file_name = 'qrcode-{order_code}.png'.format(order_code=self.code)
        qrcode_path = os.path.join(settings.MEDIA_ROOT, qrcode_file_name)

        if os.path.exists(qrcode_path):
            return qrcode_path

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        customer_info = {
            'Name': self.customer_name,
            'Phone': self.customer_phone,
            'Email': self.customer_email,
        }

        qr.add_data(customer_info)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(qrcode_path)

        return qrcode_path


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(null=True)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return self.order.code
