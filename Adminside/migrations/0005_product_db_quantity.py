# Generated by Django 4.1.2 on 2023-01-06 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminside', '0004_product_db_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_db',
            name='Quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
