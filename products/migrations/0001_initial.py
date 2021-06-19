# Generated by Django 3.2.4 on 2021-06-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('current_stock', models.IntegerField()),
            ],
        ),
    ]
