from django.urls import path
from . import views

app_name='stock'

urlpatterns = [
    path('',views.MatrialTypeListView.as_view(),name='type_list'),
    path('<int:pk>',views.MatrialTypeDetailView.as_view(),name='type_details'),
    path('create',views.MatrialTypeCreateView.as_view(),name='type_create'),
    path('update/<int:pk>',views.MatrialTypeUpdateView.as_view(),name='type_update'),
    path('delete/<int:pk>',views.MatrialTypeDeleteView.as_view(),name='type_delete'),
    
    path('category/',views.MatrialCategoryListView.as_view(),name='category_list'),
    path('category/<int:pk>',views.MatrialCategoryDetailView.as_view(),name='category_details'),
    path('category/create',views.MatrialCategoryCreateView.as_view(),name='category_create'),
    path('category/update/<int:pk>',views.MatrialCategoryUpdateView.as_view(),name='category_patient_update'),
    path('category/delete/<int:pk>',views.MatrialCategoryDeleteView.as_view(),name='category_patient_delete'),
    
]

