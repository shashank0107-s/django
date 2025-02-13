from django.db import models

# Create your models here.
#in models importted above ther class called Model 
#aotomatic orm (object relartio)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=False)
    desc = models.TextField()
    pic = models.ImageField(upload_to='products/',null=False)
    stock = models.PositiveIntegerField(default=1)
