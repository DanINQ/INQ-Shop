# Generated by Django 4.1.7 on 2023-05-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_app', '0002_alter_categories_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authors',
            name='about',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]