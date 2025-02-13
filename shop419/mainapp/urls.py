from django.urls import path #importing the path function from django

from . import views #importing the views from the mainapp to access the functions

urlpatterns = [
    path("",views.homeView,name='homepage'), #this is the path to the home page
    path("about",views.aboutView,name='aboutpage'),
    path("contacts",views.contactsView,name='contactspage')
]
