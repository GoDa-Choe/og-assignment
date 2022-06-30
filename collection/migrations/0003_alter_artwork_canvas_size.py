# Generated by Django 4.0.5 on 2022-06-29 20:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_alter_artwork_canvas_size_alter_artwork_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='canvas_size',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)]),
        ),
    ]