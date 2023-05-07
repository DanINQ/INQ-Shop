from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

# Register your models here.

admin.site.register(Categories, MPTTModelAdmin)
admin.site.register(Books)
admin.site.register(Authors)