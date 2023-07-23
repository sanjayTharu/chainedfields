from django.db import models

# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=255)
    brand=models.ForeignKey(Brand,models.DO_NOTHING)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name=models.CharField(max_length=255)
    brand=models.ForeignKey(Brand,models.DO_NOTHING)
    category=models.ForeignKey(Category,models.DO_NOTHING,blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    selling_price=models.IntegerField(blank=True,null=True)
    is_display=models.IntegerField()

    def __str__(self):
        return self.name
    