from django.contrib import admin
from django.urls import path
from Home import views
admin.site.site_header = "IceCreame Parler"
admin.site.site_title = "IceCreame Parler Admin Portal"
admin.site.index_title = "Welcome to IceCreame Parler Portal"

urlpatterns = [
    
    path("",views.index, name='Home'),
    path("about",views.about, name='about'),
     path("services",views.services, name='services'),
     path('contact/',views.contact, name='contact'),
]