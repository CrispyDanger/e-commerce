# Generated by Django 4.0.8 on 2022-12-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopping", "0002_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
