from django.db import models
from django.db.models.signals import post_save

#Each picture has a category (architectural style). Each item is linked to a category.

class Category(models.Model):
    class Meta:
        verbose_name_plural ='categories'
    name = models.CharField(max_length=32)

#Needed function to display the name e.g. in the Admin page

    def __str__(self):
      return self.name


#This class represents the image model. Each image has the following attributes (architectural style,name, description,image, category). The pictures are stored in the media folder (upload to photos -> media).
# Each Picture has a category ( analogous to architectural style   e.g   Item = Pictutre from the colosseum in Rome, Category is . The categories have been set over the Admin page.)

class Item(models.Model):

 #  ArchitecturalStyle = models.TextField(null=True, blank=True) not needed longer. Has not be deleted to possible side effects on Admin area.
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media', blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING
    )

    # Needed function to display the name e.g. in the Admin page

    def __str__(self):
        return self.name

