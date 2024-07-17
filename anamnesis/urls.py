from django.urls import path
from . import views

app_name='anamnesis'
urlpatterns = [
    path('',views.AnamnesisTypeListView.as_view(),name='anamnesis_list'),
    path('<int:pk>',views.AnamnesisTypeDetailView.as_view(),name='anamnesis_details'),
    path('create',views.AnamnesisTypeCreateView.as_view(),name='anamnesis_create'),
    path('update/<int:pk>',views.AnamnesisTypeUpdateView.as_view(),name='anamnesis_update'),
    path('delete/<int:pk>',views.AnamnesisTypeDeleteView.as_view(),name='anamnesis_delete'),
    
    path('patient/',views.AnamnesisPatientListView.as_view(),name='anamnesis_patient_list'),
    path('patient/<int:pk>',views.AnamnesisPatientDetailView.as_view(),name='anamnesis_patient_details'),
    path('patient/create',views.AnamnesisPatientCreateView.as_view(),name='anamnesis_patient_create'),
    path('patient/update/<int:pk>',views.AnamnesisPatientUpdateView.as_view(),name='anamnesis_patient_update'),
    path('patient/delete/<int:pk>',views.AnamnesisPatientDeleteView.as_view(),name='anamnesis_patient_delete'),
    
]
