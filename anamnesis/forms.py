from django import forms
from .models import Anamnesis,AnamnesisType

class AnamnesisTypeForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=AnamnesisType
        
class AnamnesisForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Anamnesis
        
class AnamnesisPatinetForm(forms.ModelForm):
    class Meta:
        exclude=('patient',)
        model=Anamnesis
