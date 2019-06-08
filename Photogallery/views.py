#Load all needed packages


from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
from Photogallery.models import Item, Category
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage


#Show all pictures on the main page. Category.objects.all will display all items from the database

def index(request):
    Category.objects.get(id=1).item_set.all()

    template = loader.get_template('templates/../index.html')
    context = {
        'categories': Category.objects.all()
    }

    return HttpResponse(template.render(context, request))


#Show Items of one category habdover with parameter 'parameter'. The function .filter(parameter) enables to load pictures only from country.

def showPicturesfromCountry(request):
    Category.objects.get(id=1).item_set.all()
    your_parameter = request.GET['parameter']
    load_country = your_parameter


    template = loader.get_template('ArchitecturalStyle_view.html')

    context = {

        'categories': Category.objects.all().filter(name=load_country)
    }

    return HttpResponse(template.render(context, request))


#Access each itam via URL localhost/item/<id>
def item(request, item_Id):
    try:
        itm = Item.objects.get(id=item_Id)
    except Item.DoesNotExist:
        itm = None

    template = loader.get_template('item.html')
    context = {
        'item': itm

    }

    return HttpResponse(template.render(context, request))


# This is the upload function. It stores a image as an instance of the class item (picture) to the database.
# The POST method is needed.  For the image upload request.Files is needed

from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Item

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Item( name=request.POST['name'],  description=request.POST['description'],    image=request.FILES['image'],  category_id=request.POST['category'])

            instance.save()
            return HttpResponseRedirect('item/')
    else:
        form = UploadFileForm()
    return render(request, 'upload_via_form.html', {'form': form})


























