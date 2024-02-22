# Generated by Django 5.0.1 on 2024-02-16 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orderapp', '0002_alter_ordermodel_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='add_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]