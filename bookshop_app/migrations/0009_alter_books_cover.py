# Generated by Django 4.1.7 on 2023-05-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_app', '0008_alter_books_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
