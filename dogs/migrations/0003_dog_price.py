# Generated by Django 5.0.1 on 2024-05-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0002_dog_is_public_dog_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='price',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
    ]
