from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AnamnesisForm,AnamnesisTypeForm
from .models import Anamnesis,AnamnesisType
from accounts.models import Patient
# Create your views here.

class AnamnesisTypeListView(LoginRequiredMixin,generic.ListView):
    template_name='anamnesis/anamnesis_list.html'
    context_object_name='anamnesis_list'
    def get_queryset(self):
        return AnamnesisType.objects.all()

class AnamnesisTypeDetailView(LoginRequiredMixin,generic.DetailView):
    template_name='anamnesis/anamnesis_details.html'
    model=AnamnesisType
    context_object_name='anamnesis'
    

class AnamnesisTypeCreateView(LoginRequiredMixin,generic.CreateView):
    form_class=AnamnesisTypeForm
    template_name='anamnesis/anamnesis_create.html'
    def get_queryset(self):
        return AnamnesisType.objects.all()
    
    def get_success_url(self):
        pk=AnamnesisType.objects.get(name=self.kwargs['name']).pk
        return reverse('anamnesis:anamnesis_details' ,args=pk)
    
class AnamnesisTypeUpdateView(LoginRequiredMixin,generic.UpdateView):
    form_class=AnamnesisTypeForm
    template_name='anamnesis/anamnesis_update.html'
    context_object_name='anamnesis'

    def get_queryset(self):
        return AnamnesisType.objects.all()
    
    def get_success_url(self):
        return reverse('anamnesis:anamnesis_details' ,args=self.request.pk)
    
class AnamnesisTypeDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name='anamnesis/anamnesis_delete.html'
    context_object_name='anamnesis'

    def get_queryset(self):
        return AnamnesisType.objects.all()
    
    def get_success_url(self):
        return reverse('anamnesis:anamnesis_list')
    
    

##################### patient anamnesis###########################

class AnamnesisPatientListView(LoginRequiredMixin,generic.ListView):
    template_name='anamnesis/anamnesis_patient_list.html'
    context_object_name='anamnesis_list'
    def get_queryset(self):
        return Anamnesis.objects.all()

class AnamnesisPatientDetailView(LoginRequiredMixin,generic.DetailView):
    template_name='anamnesis/anamnesis_patient_details.html'
    model=Anamnesis
    context_object_name='anamnesis'
    

class AnamnesisPatientCreateView(LoginRequiredMixin,generic.CreateView):
    form_class=AnamnesisForm
    template_name='anamnesis/anamnesis_patient_create.html'
    def get_queryset(self):
        return Anamnesis.objects.all()
    
    def get_success_url(self):
        pk=Anamnesis.objects.last().pk
        return reverse('anamnesis:anamnesis_patient_details' ,args=(pk,))
    
class AnamnesisPatientUpdateView(LoginRequiredMixin,generic.UpdateView):
    form_class=AnamnesisForm
    template_name='anamnesis/anamnesis_patient_update.html'
    context_object_name='anamnesis'

    def get_queryset(self):
        return Anamnesis.objects.all()
    
    def get_success_url(self):
        return reverse('anamnesis:anamnesis_patient_details' ,args=self.request.pk)
    
class AnamnesisPatientDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name='anamnesis/anamnesis_patient_delete.html'
    context_object_name='anamnesis'

    def get_queryset(self):
        return Anamnesis.objects.all()
    
    def get_success_url(self):
        return reverse('anamnesis:anamnesis_patient_list')
    