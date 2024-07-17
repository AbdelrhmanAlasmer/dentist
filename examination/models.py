from django.db import models
from django.utils.timezone import now
from treatment.models import TreatmentType
from stock.models import MatrialType

class Teeth(models.Model):
    name=models.CharField( max_length=20)
    number=models.IntegerField()

class Examination(models.Model):
    date=models.DateTimeField( default=now)
    visit=models.ForeignKey('visits.Visit',  on_delete=models.PROTECT)
    note=models.TextField()
    
class PatientProblem(models.Model):
    examination=models.ForeignKey(Examination, on_delete=models.CASCADE)
    problem_description=models.TextField()
    default_cost=models.DecimalField( max_digits=6, decimal_places=2)
    teeth=models.ForeignKey(Teeth, on_delete=models.PROTECT)
    defaultTreatment = models.ForeignKey(TreatmentType, on_delete=models.CASCADE, related_name='default_patient_problems')
    treatment = models.ForeignKey(TreatmentType, on_delete=models.CASCADE, related_name='patient_problems')
    is_up=models.BooleanField(default=False)
    is_child=models.BooleanField(default=False)
    addtional_treatment=models.TextField()
    is_treated=models.BooleanField(default=False)

class ProblemNeededMatrial(models.Model):
    treatment_done=models.ForeignKey(PatientProblem, on_delete=models.CASCADE)
    matrial=models.ForeignKey(MatrialType, on_delete=models.CASCADE)
    notes=models.TextField() 

