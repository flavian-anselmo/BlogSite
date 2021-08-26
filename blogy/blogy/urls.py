"""blogy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    #pattern to our portfolio app 
    #the code aso includes all the urls in the portfolio app 
    #hence they are accessed when prefixed portfolio/
    path('portfolio/',include('portfolio.urls')),
    path('myblogs/',include('myblogs.urls')),
    path('admin/', admin.site.urls),
    #path('',views.index,name='index')
]
"""
this url is project based moves to the specific call in the app urls and
hence calling the appropriate view method hence rendering a template

this acts as the table of content of the website since once we have many aplications 
hence more urls for our case we have the portfolio app here  and the django admin app

path('path/',include('appname.urls'))
include include the app as a urls in the website 
"""
