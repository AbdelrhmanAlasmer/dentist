from django import forms
from .models import MatrialCategory,MatrialType


class MatrialCategoryForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=MatrialCategory
        
class MatrialTypeForm(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=MatrialType
        

