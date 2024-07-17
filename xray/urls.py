from django.urls import path
from . import views

app_name='xray'
urlpatterns = [
    path('',views.XrayListView.as_view(),name='xray_list'),
    path('<int:pk>',views.XrayDetailView.as_view(),name='xray_details'),
    path('create',views.XrayCreateView.as_view(),name='xray_create'),
    path('update/<int:pk>',views.XrayUpdateView.as_view(),name='xray_update'),
    path('delete/<int:pk>',views.XrayDeleteView.as_view(),name='xray_delete'),
]
