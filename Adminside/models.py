from django.db import models

# Create your models here.
class admin_db(models.Model):
    Name=models.CharField(max_length=15,null=True,blank=True)
    Email_id=models.EmailField(null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)
    Address=models.TextField(max_length=20,null=True,blank=True)

class category_db(models.Model):
    C_Name=models.CharField(max_length=20,null=True,blank=True)
    Descr=models.CharField(max_length=30,null=True,blank=True)
    C_Image=models.ImageField(upload_to="profile",null=True,blank=True)

class product_db(models.Model):
    P_Name=models.CharField(max_length=20,null=True,blank=True)
    Description=models.CharField(max_length=30,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Category=models.CharField(max_length=20,null=True,blank=True)
    P_Img=models.ImageField(upload_to="profile",null=True,blank=True)

class contact_db(models.Model):
    Name=models.CharField(max_length=25,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Sub=models.CharField(max_length=100,null=True,blank=True)
    Msg=models.CharField(max_length=150,null=True,blank=True)
