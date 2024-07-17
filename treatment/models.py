from django.db import models
from stock.models import MatrialType

#have all way of treatment 
class TreatmentType(models.Model):
    name=models.CharField( max_length=20)
    description=models.TextField()
    
    
    
#the default related matrial to treatment are consumed 
class TreatmentDefaultMatrial(models.Model):
    treatment=models.ForeignKey(TreatmentType, on_delete=models.CASCADE)
    matrial=models.ForeignKey(MatrialType, on_delete=models.CASCADE) 

    
