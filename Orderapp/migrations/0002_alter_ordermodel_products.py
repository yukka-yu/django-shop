# Generated by Django 5.0.1 on 2024-02-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orderapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='products',
            field=models.ManyToManyField(related_name='products', to='Orderapp.productmodel'),
        ),
    ]
