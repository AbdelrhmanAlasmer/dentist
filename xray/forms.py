from django import forms
from .models import Xray

class XrayForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=Xray