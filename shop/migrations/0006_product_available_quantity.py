# Generated by Django 3.0.2 on 2020-05-13 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200512_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available_quantity',
            field=models.IntegerField(default=100),
        ),
    ]
