# Generated by Django 3.2 on 2021-04-25 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_location_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='image_url',
        ),
    ]
