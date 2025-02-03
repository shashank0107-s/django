from django.db import models

# Create your models here.
3 #in models importted above ther class called Model 
#aotomatic orm (object relartio)

class Product(models.model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=false)
    desc = models.TextField()
    pic = models.ImageField(upload_to='products/',null=false)
    stock = models.PositiveIntegerField(default=1)
