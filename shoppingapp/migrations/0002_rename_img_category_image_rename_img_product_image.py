# Generated by Django 4.2.6 on 2023-10-25 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]
