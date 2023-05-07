# Generated by Django 4.1.7 on 2023-05-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop_app', '0010_alter_authors_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='type',
            field=models.CharField(choices=[('Paperback', 'Paperback'), ('Hardback', 'Hardback'), ('Leather', 'Leather')], max_length=20),
        ),
    ]