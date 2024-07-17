from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import XrayForm
from .models import Xray
from django.urls import reverse

class XrayListView(LoginRequiredMixin,generic.ListView):
    template_name='xray/xray_list'
    context_object_name='xray'
    def get_queryset(self):
        return Xray.objects.all()

class XrayDetailView(LoginRequiredMixin,generic.DetailView):
    template_name='xray/xray_details.html'
    context_object_name='xray'
    def get_queryset(self):
        return Xray.objects.all()
    

class XrayCreateView(LoginRequiredMixin,generic.CreateView):
    form_class=XrayForm
    template_name='xray/xray_create.html'
    def get_queryset(self):
        return Xray.objects.all()
    
    def get_success_url(self):
        pk=Xray.objects.order_by('-pk').first().pk
        return reverse('xray:xray_details' ,args=pk)
    
class XrayUpdateView(LoginRequiredMixin,generic.UpdateView):
    form_class=XrayForm
    template_name='xray/xray_update.html'
    context_object_name='xray'

    def get_queryset(self):
        return Xray.objects.all()
    
    def get_success_url(self):
        return reverse('xray:xray_details' ,args=self.request.pk)
    
class XrayDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name='xray/xray_delete.html'
    context_object_name='xray'

    def get_queryset(self):
        return Xray.objects.all()
    
    def get_success_url(self):
        return reverse('xray:xray_list')