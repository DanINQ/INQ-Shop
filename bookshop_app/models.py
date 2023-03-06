from django.db import models

# Create your models here.

class SpecialOffers(models.Model):


class Books(models.Model):
    title = models.CharField(max_length=30, blank=False)
    author = models.CharField(max_length=30, blank=False)
    price = models.IntegerField()
    cover = models.FileField(upload_to='uploads/')
    description = models.CharField(max_length=200, blank=False)
    publish_date = models.CharField(max_length=20)
class Authors(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=400)

class Cart(models.Model):
    pass
