# Generated by Django 4.0.7 on 2022-09-21 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_products_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='sluge',
            new_name='slug',
        ),
    ]