# Generated by Django 3.2.5 on 2021-07-06 11:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_photos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='photos',
        ),
        migrations.AlterField(
            model_name='imagepost',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]