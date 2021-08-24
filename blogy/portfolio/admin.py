from django.contrib import admin
from portfolio.models  import Project

# Register your models here.
class PostProject(admin.ModelAdmin):
    pass
admin.site.register(Project,PostProject)
"""
creating the admin panel for the project 
we have to register the data models that are
like our tables in the database in to the Admin
THis allows as to have input fields in the admin panel
for us to update the content dynamically  
"""