from django.urls import path
from . import views as views
urlpatterns = [
	#this are  the paths to the views 
	#the first path is to the forst view 
	#the second path is to the second which fetches as per the id 
	path('', views.project,name="project"),
	path('<int:pk>/', views.project_details,name='project_details')

]
"""
browser--->views-->urls
browser gets the response from the view.py
the brwser initially sends a request to the urls.py file  
the file looks at the url patttern and decides which method to fire
inn the views.py file 

path('',views.nameOfTheViwe,name='nameofmethod')
-make sure the path module from django.urls is imported 
-import the views form the views.py file for us to
	be able o access the methods to render tempeleates  
 
 to get data as per the primary key use 
 path(<int:pk>/,)
 <int:pk> notation tells django that the value passed is an intenger 
 and that signifies the position of the project in the data base 
 
"""