from django.contrib import admin
from . import views
from django.urls import include,path

urlpatterns = [
   
    path('',views.index,name='index'),
]
"""
this is added in the app to call the method responsible
for the view hwnce rendering a template to the user
"""