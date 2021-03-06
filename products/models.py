from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=100, unique=True, help_text='Alphabets and digits mix')
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    unit_price = models.IntegerField()
    current_stock = models.IntegerField()

    def __str__(self):
        return self.code + "-" + self.name
