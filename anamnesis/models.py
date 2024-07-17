from django.db import models
from accounts.models import Patient


class AnamnesisType(models.Model):
    name=models.CharField( max_length=50,db_index=True)
    description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name

class Anamnesis(models.Model):
    patient=models.ForeignKey(Patient,null=True,blank=True ,on_delete=models.CASCADE)
    anamnesis_type=models.ForeignKey(AnamnesisType,on_delete=models.DO_NOTHING)
    patient_description=models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.patient.full_name 
       
