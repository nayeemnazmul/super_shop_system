import os

import qrcode
from qrcode.image.svg import SvgPathImage
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

    # pdf needs full path of generated svg file to render correctly
    @property
    def customer_info_in_qrcode_path(self):
        qrcode_file_name = 'qrcode-{order_code}.svg'.format(order_code=self.code)
        qrcode_url = os.path.join(settings.MEDIA_URL, qrcode_file_name)
        qrcode_path = os.path.join(settings.MEDIA_ROOT, qrcode_file_name)

        try:
            os.mkdir(settings.MEDIA_ROOT)
        except FileExistsError:
            if os.path.isfile(qrcode_path):
                return qrcode_path
            else:
                self.generate_qrcode_for_customer_info(qrcode_path)
                return qrcode_path

    # TODO to show svg in html correctly, url-format: /media/example.svg
    # @property
    # def customer_info_in_qrcode_url(self):
    #     pass

    def generate_qrcode_for_customer_info(self, qrcode_path):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
            image_factory=SvgPathImage,
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


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField(null=True)

    class Meta:
        unique_together = ('order', 'product')

    def __str__(self):
        return self.order.code
