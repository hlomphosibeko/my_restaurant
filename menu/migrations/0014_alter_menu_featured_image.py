# Generated by Django 4.2.20 on 2025-03-18 21:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0013_delete_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="featured_image",
            field=cloudinary.models.CloudinaryField(
                default="placeholder", max_length=255, verbose_name="image"
            ),
        ),
    ]
