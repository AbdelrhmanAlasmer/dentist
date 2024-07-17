from django.db import models

class Xray(models.Model):
    visit=models.ForeignKey('visits.Visit', on_delete=models.CASCADE)
    xray_photo=models.ImageField(upload_to='xray/%Y/%m/%d',null= True,blank=True, height_field=None, width_field=None, max_length=None)
    xray_url=models.URLField( max_length=200)