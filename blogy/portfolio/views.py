from django.shortcuts import render
from portfolio.models import Project
#import the models.py file to use the class models
def project(request):
	projects=Project.objects.all()
	#the obove code is a query to the database 
	"""
	simply tells the database to retrieve all the object
	records form the specific table present  
	"""
	context={
		'projects':projects
	}
	#render the template in context with our projects present in the database 
	return render(request,'project.html',context)

	"""
	in the code block above we define a dictionary context 
	the dictionary only has one entry projects to which we assign our 
	Queryset containing all projects ,the context is used to send the info 
	to our tenmplate ,every view we create needs to have a context dictionary 
	"""

def project_details(request,pk):
	#retrive as the primary key pk 
	project=Project.objects.get(pk=pk)
	"""[we perform another quesry on
	this query retrieves the project with primary key indx 
	we then assign that project to another context dictionary which we assign
	pass to render ]

	Returns:
		[string]: [return all records in the db as per the primary key]
	"""
 
 
 
	context={
		#name of the app and the var name for the DB records 
		'project':project
	}
	#remder the template to the user 
 
	return render(request,'details.html',context)