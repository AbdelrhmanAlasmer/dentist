from django.db import models
from django.utils.timezone import now
from accounts.models import Patient,Employee,Doctor
from xray.models import Xray
class Visit(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist=models.ForeignKey(Doctor,  on_delete=models.PROTECT)
    employee=models.ForeignKey(Employee, on_delete=models.PROTECT)
    time_date=models.DateTimeField(default=now)
    payments=models.DecimalField( max_digits=8, decimal_places=2)
    next_visit=models.DateTimeField(null=True ,blank=True)
    spended_time=models.CharField(max_length=10)
    notes=models.TextField()
    
class  VisitTreatmentDone(models.Model):
    visit=models.OneToOneField(Visit, on_delete=models.CASCADE)
    problem=models.ForeignKey('examination.PatientProblem', on_delete=models.PROTECT)
    action_description=models.TextField()

class VisitXray(models.Model):
    visit=models.ForeignKey(Visit, on_delete=models.CASCADE)
    xray=models.ForeignKey(Xray,on_delete=models.CASCADE)
    