from django.urls import path
from . import views

urlpatterns = [
	#thsi are the patterns for the app 
	path('',views.fetchAllBlogs,name="fetcAllBlogs"),
	path('<int:pk>/',views.fetchByPrimarykey,name="fetchByPrimarykey"),
	path('<category>/',views.fecthByCategory,name="fecthByCategory")
	
	
 
]
"""this is like the tbl of content for the 
web application since it will help in rendering the uis 
"""