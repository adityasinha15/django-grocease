# Generated by Django 3.0.2 on 2020-05-15 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20200514_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='p_id',
            field=models.IntegerField(default=100),
        ),
    ]
