from django.shortcuts import render
from .models import MatrialCategory,MatrialType
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MatrialCategoryForm,MatrialTypeForm
from django.urls import reverse

# Create your views here.
class MatrialCategoryListView(LoginRequiredMixin,generic.ListView):
    template_name='stock/category_list.html'
    context_object_name='matrial_category'
    def get_queryset(self):
        return MatrialCategory.objects.all()

class MatrialCategoryDetailView(LoginRequiredMixin,generic.DetailView):
    template_name='stock/category_details.html'
    context_object_name='matrial_category'
    def get_queryset(self):
        return MatrialCategory.objects.all()
    

class MatrialCategoryCreateView(LoginRequiredMixin,generic.CreateView):
    form_class=MatrialCategoryForm
    template_name='stock/category_create.html'
    def get_queryset(self):
        return MatrialCategory.objects.all()
    
    def get_success_url(self):
        pk=MatrialCategoryForm.objects.order_by('-pk').first().pk
        return reverse('stock:category_details' ,args=pk)
    
class MatrialCategoryUpdateView(LoginRequiredMixin,generic.UpdateView):
    form_class=MatrialCategoryForm
    template_name='stock/category_update.html'
    context_object_name='matrial_category'

    def get_queryset(self):
        return MatrialCategory.objects.all()
    
    def get_success_url(self):
        return reverse('stock:category_details' ,args=self.request.pk)
    
class MatrialCategoryDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name='stock/category_delete.html'
    context_object_name='matrial_category'

    def get_queryset(self):
        return MatrialCategory.objects.all()
    
    def get_success_url(self):
        return reverse('stock:category_list')
    
    

##################### patient anamnesis###########################

class MatrialTypeListView(LoginRequiredMixin,generic.ListView):
    template_name='stock/type_list.html'
    context_object_name='matrial_type'
    def get_queryset(self):
        return MatrialType.objects.all()

class MatrialTypeDetailView(LoginRequiredMixin,generic.DetailView):
    template_name='stock/type_details.html'
    context_object_name='matrial_type'
    def get_queryset(self):
        return MatrialType.objects.all()
    

class MatrialTypeCreateView(LoginRequiredMixin,generic.CreateView):
    form_class=MatrialTypeForm
    template_name='stock/type_create.html'
    def get_queryset(self):
        return MatrialType.objects.all()
    
    def get_success_url(self):
        pk=MatrialTypeForm.objects.order_by('-pk').first().pk
        return reverse('stock:type_details' ,args=pk)
    
class MatrialTypeUpdateView(LoginRequiredMixin,generic.UpdateView):
    form_class=MatrialTypeForm
    template_name='stock/type_update.html'
    context_object_name='matrial_type'

    def get_queryset(self):
        return MatrialType.objects.all()
    
    def get_success_url(self):
        return reverse('stock:type_details' ,args=self.request.pk)
    
class MatrialTypeDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name='stock/type_delete.html'
    context_object_name='matrial_type'

    def get_queryset(self):
        return MatrialType.objects.all()
    
    def get_success_url(self):
        return reverse('stock:type_list')