from django.db import models

# Create your models here.
class reg_db(models.Model):
    Username=models.CharField(max_length=25,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password=models.TextField(max_length=20,null=True,blank=True)
    C_Password=models.TextField(max_length=20,null=True,blank=True)

class cart_db(models.Model):
    Name=models.CharField(max_length=20,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)

