from django.db import models
class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	technology=models.CharField(max_length=100)
	#image = models.FilePathField(pathr="/images")
	githubLink=models.CharField(max_length=200)

# Create your models here.
"""
if you want to store data to display in data base then you will use
need a database 
we need to use sql to manage the database but in django we can use ORM
we can create pyclasses to represent the tables in the database ..for our
case we only need on table to store info for the projects 	
NOTE 
-EAch model maps to a single table in the database 
the class attributes will be the table fields 
title ,description,technology,githublink

"""
