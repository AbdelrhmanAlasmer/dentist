from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Employee)
admin.site.register(PatientFamily)

