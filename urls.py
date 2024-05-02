from django.contrib import admin
from django.urls import path
from petstoreapp import views 
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
  
    path('dashboard',views.dashboard),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('demo',views.demo),
    path('',views.home),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

