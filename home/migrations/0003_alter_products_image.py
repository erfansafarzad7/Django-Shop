# Generated by Django 4.1.1 on 2022-09-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products/%Y/%m/%d/'),
        ),
    ]
