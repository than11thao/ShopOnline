# Generated by Django 4.2.3 on 2023-08-06 11:40

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_cartorderitems_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorderitems',
            name='image',
            field=models.ImageField(default='product.png', upload_to=core.models.user_directory_path),
        ),
    ]
