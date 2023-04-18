from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class SpecialOffers(models.Model):
    pass


class Authors(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=400)


class Categories(models.Model):
    category = models.CharField(max_length=30, null=False, blank=False)
    type = models.CharField(max_length=11, choices=[
        ('NF', 'Non-Fiction'),
        ('FI', 'Fiction')
    ], null=False, blank=False)


class Books(models.Model):
    title = models.CharField(max_length=30, blank=False)
    language = models.CharField(max_length=10, blank=False)
    author = models.ManyToManyField(Authors)
    price = models.IntegerField()
    cover = models.ImageField(upload_to='uploads/')
    description = models.CharField(max_length=200, blank=False)
    publish_date = models.CharField(max_length=20)
    category = models.ManyToManyField(Categories)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    closed = models.BooleanField(default=False)


class OrderItem(models.Model):
    product = models.ForeignKey(Books, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
