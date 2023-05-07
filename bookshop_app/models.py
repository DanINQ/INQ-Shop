from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class SpecialOffers(models.Model):
    pass


class Authors(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Categories(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=100,)
    language = models.CharField(max_length=10)
    author = models.ManyToManyField(Authors)
    price = models.IntegerField()
    cover = models.ImageField(null=True, blank=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    number_of_pages = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=20, choices=[
        ('Paperback', 'Paperback'),
        ('Hardback', 'Hardback'),
        ('Leather', 'Leather')
    ])
    description = models.CharField(max_length=10000)
    publish_date = models.CharField(blank=True, null=True, max_length=20)
    category = models.ManyToManyField(Categories)

    def __str__(self):
        return self.title


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
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
