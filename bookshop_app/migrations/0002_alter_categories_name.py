# Generated by Django 4.1.7 on 2023-05-01 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
