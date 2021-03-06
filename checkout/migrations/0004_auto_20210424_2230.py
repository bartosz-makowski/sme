# Generated by Django 3.2 on 2021-04-24 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210424_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='postcode',
            field=models.CharField(blank=True, default='Postcode', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address1',
            field=models.CharField(default='Street Address 1', max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(default='Town or City', max_length=40),
        ),
    ]
