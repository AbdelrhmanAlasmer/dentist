from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
User=get_user_model()
from .forms import (PatientModelForm,CustomUserCreationForm,FamilyModelForm,DoctorModelForm,EmployeeModelForm,
                    DoctorCreateModelForm,EmployeeCreateModelForm)
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Patient,Doctor,Employee
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from anamnesis.models import Anamnesis
from anamnesis.forms import AnamnesisPatinetForm
class LoginView(LoginView):
    template_name='auth/login.html'

class LogoutView(LogoutView):
    template_name='landing.html'
    
class UserCreationView(LoginRequiredMixin,generic.CreateView):
    template_name='auth/signup.html'
    form_class=CustomUserCreationForm
    
    def get_success_url(self):
        return reverse('login')


class LandingTemplateView(generic.TemplateView):
    template_name='landing.html'

class PatientListView(LoginRequiredMixin,generic.ListView):
    model=Patient
    template_name='account/patient_list.html'
    context_object_name='patient_list'

class PatientCreateView(LoginRequiredMixin,generic.CreateView):
    form_class=PatientModelForm
    template_name='account/create.html'
    def get_success_url(self):
        pk=Patient.objects.last().pk
        return reverse('account:details',args=(pk,))
    
class PatientDetailView(LoginRequiredMixin,generic.DetailView):
    model=Patient
    template_name='account/details.html'
    context_object_name='patient'
    
class PatientUpdateView(LoginRequiredMixin,generic.UpdateView):
    form_class=PatientModelForm
    template_name='account/update.html'
    
    def get_queryset(self):
        # initial queryset of leads for the entire organisation
        return Patient.objects.all()
    def get_success_url(self):
        pk=self.kwargs['pk']
        return reverse('account:details',args=(pk,))
class PatientDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name='account/delete.html'
    def get_queryset(self):
        # initial queryset of leads for the entire organisation
        return Patient.objects.all()
    def get_success_url(self):
        return reverse('account:list')
    
def landing_page(request):
    return render(request,'landing.html')



# to create the frist incoming patient form
#not finished yet

""" 

@login_required
def patinet_anamnesis_create_view(request):
    patient_form=PatientModelForm
    anamnesis_form=AnamnesisPatinetForm
    if request.method == 'POST':
        patient_form=PatientModelForm(request.POST)
        anamnesis_form=AnamnesisPatinetForm(request.POST)
        if patient_form.is_valid() and anamnesis_form.is_valid():
            patient_form.save( commit=True)
            try:
                patient = Patient.objects.order_by('-created_date').first()
            except patient.DoesNotExist:
        # Handle the case where the user with the given email doesn't exist
        # (e.g., show an error message or redirect to a different page)
                pass
            else:
                anamnesis_form.save(commit= False)
                if anamnesis_form.is_valid():
                    Anamnesis.objects.create(
                        patient=patient,
                        anamnesis_type = anamnesis_form.cleaned_data['anamnesis_type'],
                        patient_description = anamnesis_form.cleaned_data['patient_description']
                    )
                return redirect('account:list')# redirect to the page that handel the visits
    context={
        'userForm':patient,
        'doctorForm':an     
    }
    
    return render(request,'account/doctor_create.html',context) """
       
""" @login_required
def patient_user_create_view(request):
    family_form=FamilyModelForm
    patient_form=PatientModelForm
    if request.method == 'POST':
        if request.POST['parent']:    
            family_form=FamilyModelForm(request.POST)
            family_form.save()
        patient_form=PatientModelForm(request.POST)
         
        patient_form.patient_Family=
        
    context={
        'familyForm':family_form,
        'patinerForm':patient_form        
    }
    
    return render(request,'account/patient_create.html',context) """


""" def Patientcreate(request):
    form=PatientModelForm()
    if request.method == 'POST':
        form=PatientModelForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            phone1=form.cleaned_data['phone1']
            phone2=form.cleaned_data['phone2']
            email=User.objects.first()
            patient=Patient.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone1=phone1,
                phone2=phone2,
                email=email
            )
    context={
        'from':form
    }
    return render(request,'dashboard.html',context)
 """
def patientList(request):
    query_set=Patient.objects.all()
    context={
        'data':query_set
    }
    return render(request,'account/dashboard.html',context)

def patientdetails(request,pk):
    query_set=Patient.objects.get(pk=pk)
    context={
        'data':query_set
    }
    return render(request,'account/details.html',context)

def patient_create(request):
    form=PatientModelForm()
    
    if request.method == 'POST':
        form=PatientModelForm(request.POST)
        if form.is_valid():
            form.save()
            last=Patient.objects.last()
            return redirect(f'/account/{last.pk}')
    context={
        'form':form
    }
    return render(request,'account/create.html',context)
    
def patient_update(request,pk):
    patient=Patient.objects.get(pk=pk)
    form=PatientModelForm(instance=patient)
    return_path=reverse('account:details',args=(patient.pk,))
    if request.method == 'POST':
        form=PatientModelForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect(f'/account/{pk}')
    context={
        'form':form,
        'data':patient,
        'return':return_path
    }
    return render(request,'account/update.html',context)
def patient_delete(request,pk):
    patient=Patient.objects.get(pk=pk)
    patient.delete()
    return redirect('/account')
    


###############################################################
      ##############  doctor views ######################
###############################################################


@login_required
def doctor_user_create_view(request):
    user_from=CustomUserCreationForm
    doctor_form=DoctorCreateModelForm
    if request.method == 'POST':
        user_from=CustomUserCreationForm(request.POST)
        doctor_form=DoctorCreateModelForm(request.POST)
        if doctor_form.is_valid() and user_from.is_valid():
            user_from.save( commit=True)
            try:
                user = User.objects.get(email=request.POST['email'])
            except User.DoesNotExist:
        # Handle the case where the user with the given email doesn't exist
        # (e.g., show an error message or redirect to a different page)
                pass
            else:
                doctor_form.save(commit= False)
                if doctor_form.is_valid():
                    Doctor.objects.create(
                        doc_email=user,
                        first_name = doctor_form.cleaned_data['first_name'],
                        last_name = doctor_form.cleaned_data['last_name']
                    )
                return redirect('account:doctor_list')
        
    context={
        'userForm':user_from,
        'doctorForm':doctor_form     
    }
    
    return render(request,'account/doctor_create.html',context)


class DoctorListView(LoginRequiredMixin,generic.ListView):
    template_name='account/doctor_list.html'  
    context_object_name='doctors_list'
    def get_queryset(self):
        queryset=Doctor.objects.all()
        return queryset
    
class DoctorDetailsView(LoginRequiredMixin,generic.DetailView):
    template_name='account/doctor_details.html'  
    context_object_name='doctor'
    def get_queryset(self):
        queryset=Doctor.objects.all()
        return queryset
    
class DoctorupdateView(LoginRequiredMixin,generic.UpdateView):
    template_name='account/doctor_update.html'  
    form_class=DoctorModelForm
    
    def get_queryset(self):
        queryset=Doctor.objects.all()
        return queryset
    def get_success_url(self):
        pk=self.kwargs['pk']
        return reverse('account:doctor_details',args=(pk,))

class DoctorDeleteView(LoginRequiredMixin,generic.DeleteView):    
    template_name='account/doctor_delete.html'
    
    def get_queryset(self):
        queryset=Doctor.objects.all()
        return queryset
    
    def get_success_url(self) :
        return reverse('account:doctor_list')
    
    
    
    
###############################################################
      ##############  employee views ######################
###############################################################

@login_required
def employee_user_create_view(request):
    user_from=CustomUserCreationForm
    employee_form=EmployeeCreateModelForm
    if request.method == 'POST':
        user_from=CustomUserCreationForm(request.POST)
        employee_form=EmployeeCreateModelForm(request.POST)
        if employee_form.is_valid() and user_from.is_valid():
            user_from.save( commit=True)
            try:
                user = User.objects.get(email=request.POST['email'])
            except User.DoesNotExist:
        # Handle the case where the user with the given email doesn't exist
        # (e.g., show an error message or redirect to a different page)
                pass
            else:
                employee_form.save(commit= False)
                if employee_form.is_valid():
                    Employee.objects.create(
                        emp_email=user,
                        first_name = employee_form.cleaned_data['first_name'],
                        last_name = employee_form.cleaned_data['last_name'])
                    
                return redirect('account:employee_list')
        
    context={
        'userForm':user_from,
        'employeeForm':employee_form     
    }
    
    return render(request,'account/employee_create.html',context)


class EmployeeListView(LoginRequiredMixin,generic.ListView):
    template_name='account/employee_list.html'  
    context_object_name='employee_list'
    def get_queryset(self):
        queryset=Employee.objects.all()
        return queryset
    
class EmployeeDetailsView(LoginRequiredMixin,generic.DetailView):
    template_name='account/employee_details.html'  
    context_object_name='employee'
    def get_queryset(self):
        queryset=Employee.objects.all()
        return queryset
    
class EmployeeupdateView(LoginRequiredMixin,generic.UpdateView):
    template_name='account/employee_update.html'  
    form_class=EmployeeModelForm
    
    def get_queryset(self):
        queryset=Employee.objects.all()
        return queryset
    def get_success_url(self):
        pk=self.kwargs['pk']
        return reverse('account:employee_details',args=(pk,))

class EmployeeDeleteView(LoginRequiredMixin,generic.DeleteView):
    template_name='account/employee_delete.html'
    
    def get_queryset(self):
        queryset=Employee.objects.all()
        return queryset
    
    def get_success_url(self) :
        return reverse('account:employee_list')