from django.db import models





class MatrialCategory(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField(null=True,blank=True)
    
    

class MatrialType(models.Model):
    category=models.ForeignKey(MatrialCategory,  on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    descripttion=models.TextField(null=True,blank=True)
    cost=models.DecimalField(max_digits=7,decimal_places=2)
    stock=models.IntegerField()
    
    