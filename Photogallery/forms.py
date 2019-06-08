from django import forms
from Photogallery.models import Item
from django import forms
from django.forms import ModelForm


#This form is needed to forward the data files from the model Item. With the fields the attributes of the class item is defined.

class UploadFileForm(ModelForm):
  class Meta:
    model =Item
    fields = ['name', 'description', 'image', 'category']

form = UploadFileForm()










