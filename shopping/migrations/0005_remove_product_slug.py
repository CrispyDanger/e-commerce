# Generated by Django 4.0.8 on 2022-12-02 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shopping", "0004_category_slug_product_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="slug",
        ),
    ]
