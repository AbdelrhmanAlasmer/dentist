
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import LandingTemplateView,LoginView,LogoutView,UserCreationView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('signup',UserCreationView.as_view(),name='signup'),
    path('',LandingTemplateView.as_view(),name='landing'),
    path('account/',include('accounts.urls')),  
    path('anamnesis/',include('anamnesis.urls')),
    path('stock/',include('stock.urls')),
    path('treatment/',include('treatment.urls')),
    path('xray',include('xray.urls')),
    
    
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


