from django.forms import  ModelForm
from django import forms
from .models import Patient,PatientFamily,Doctor,Employee
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.forms import UserCreationForm,UsernameField

""" class PatientForm(forms.Form):
    patient_Family=forms.CharField( required=False)
    email=forms.CharField(required=False)
    first_name=forms.CharField( max_length=10)
    last_name=forms.CharField(max_length=10)
    phone1=forms.CharField(max_length=15)
    phone2=forms.CharField(max_length=15)
     """
""" class PatientModelForm(ModelForm):
    class Meta:
        model=Patient
        fields='__all__' """


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        field_classes = {"username": UsernameField}

class PatientModelForm(ModelForm):
    class Meta:
        model= Patient
        fields=('patient_Family','first_name','last_name','phone1','phone2','date_examination','birth_day',)
        

class FamilyModelForm(ModelForm):
    class Meta:
        model=PatientFamily
        fields='__all__'
        
        
class DoctorModelForm(ModelForm):
     class Meta:
        model=Doctor
        fields='__all__'
        
class DoctorCreateModelForm(ModelForm):
     class Meta:
        model=Doctor
        fields='__all__'
        widgets = {'doc_email': forms.HiddenInput()}
        

        
class EmployeeModelForm(ModelForm):
     class Meta:
        model=Employee
        fields='__all__'

class EmployeeCreateModelForm(ModelForm):
     class Meta:
        model=Employee
        fields='__all__'
        widgets = {'emp_email': forms.HiddenInput()}