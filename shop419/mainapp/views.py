from django.shortcuts import render
from .models import Product

# to help load the template file
from django.template import loader

#to help return an http response to the user for any given request
from django.http import HttpResponse
# Create your views here.

def homeView(request):
    #querying the database and getting a collection of products class objecs from the records
    products = Product.objects.all()

    #creating a context dictionary to be used to render the template with info
    context = {
        'product_list': products, #the key we create here,
                                    #will be availlable

        'current_page': 'home'
    }
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))


def aboutView(request):
    context = {
        'current_page' : 'about'

    }
    template = loader.get_template('about.html')
    return HttpResponse(template.render(context, request))

def contactsView(request):
    context = {
        
                     

    }
    template = loader.get_template('contacts.html')
    return HttpResponse(template.render(context, request))