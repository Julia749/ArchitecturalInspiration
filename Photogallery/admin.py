from django.contrib import admin

# Register your models here to upload instances of classes it in the Admin area
from Photogallery.models import Item, Category

admin.site.register(Item)
admin.site.register(Category)
