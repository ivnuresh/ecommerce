# Generated by Django 4.2.6 on 2023-10-25 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingapp', '0002_rename_img_category_image_rename_img_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desc',
            new_name='description',
        ),
    ]
