from django.urls import path
from . import views 

app_name='account'
urlpatterns = [
    path('',views.PatientListView.as_view(),name='list'),
    path('<int:pk>',views.PatientDetailView.as_view(),name='details'),
    path('create',views.PatientCreateView.as_view(),name='create'),
    path('update/<int:pk>',views.PatientUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.PatientDeleteView.as_view(),name='delete'),
 
     
    path('doctor/',views.DoctorListView.as_view(),name='doctor_list'),
    path('doctor/<int:pk>',views.DoctorDetailsView.as_view(),name='doctor_details'),
    path('doctor/create',views.doctor_user_create_view,name='doctor_create'),
    path('doctor/update/<int:pk>',views.DoctorupdateView.as_view(),name='doctor_update'),
    path('doctor/delete/<int:pk>',views.DoctorDeleteView.as_view(),name='doctor_delete'),

    
    path('employee/',views.EmployeeListView.as_view(),name='employee_list'),
    path('employee/<int:pk>',views.EmployeeDetailsView.as_view(),name='employee_details'),
    path('employee/create',views.employee_user_create_view,name='employee_create'),
    path('employee/update/<int:pk>',views.EmployeeupdateView.as_view(),name='employee_update'),
    path('employee/delete/<int:pk>',views.EmployeeDeleteView.as_view(),name='employee_delete'),
   
]

