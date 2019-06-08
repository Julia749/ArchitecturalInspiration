"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Photogallery import views


# In the URLs.py it is defined which adress can be inserted in the browser and which functionaliy from the views.py will be called.
#for each item a URL will be generated

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^item/(?P<item_Id>[0-9]+)', views.item, name='item'),

url('uploadform/', views.upload_file, name='uploadform'),
url('ArchitecturalStyle_View/', views.showPicturesbyStyle, name='ArchitecturalStyle_view'),



]
