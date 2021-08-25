from django.db import models
class Category(models.Model):
    catgoryName=models.CharField(max_length=100)
    #category name of a specific blog 
class Post(models.Model):
    #this model represents the posts 
    title=models.CharField(max_length=100)
    blog=models.TextField()
    createdOn=models.DateTimeField(auto_now_add=True)
    lastModified=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField('Category',related_name='posts')    

class Comment(models.Model):
    #this represents users comments 
    author=models.CharField(max_length=100)
    comment=models.TextField()
    createdOn=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey('Post',on_delete=models.CASCADE)
    
    
    
    
    
    
"""
category model has only the name of the category 
we need a single charfield that we store the name of the category
options in lastmodified and created on fields
auto_now_add=True
this assigns current date and time to this field whenever an instance of this class
is created 
auto_now=true
assigns the current date and time to this field whenever an instance of this field
whenever you edit an instance of this class ,,the date odified is updated
   
 manyto many field takes two arguments the first is the model which the
 relationship is in this case its category The second allows us to access the relationship 
 form a category object even though we havent added a field there by adding a related    

in the comment model we have foreigh key that creates a many to one  
since one post equals many comments but no the other way round 
we cant have many posts with one comment

on_delete=models.CASCADE is used to delete the the comment instance if
the posts is deleted form the database  

HOW TO UNDERSTAND MANY TO ONE RELATIONSHIP
{
    USE django.db.models.ForeignKey
    it requires a positional argument :the class or 
    table to which the table is related
    
    for example you have two tables and hence one depends on another to display data
    eg a table car_tbl and manufacturer
    you can have many cars but each have only one manufacturer
    hence a many to one relationship
    
    hence the cartable depends on the manufacturer table to display a manufacturer
    hence the car table will have a field to input a manufacturer
    eg{
        manufacturer=models.ForeignKey('manufacturer_tbl', on_delete=models.CASCADE)
    }   
}

HOW TO UNDERSTAND MANY TO MANY RELATIONSHIP 
{
    TO define many to many relaionship
    use manyTomany field 
    for example you have a tbl teacher and tble stream in
    a school set db
    the teachers tbl requires to be assigned a stream  hence
    the teacher table will have a field stream  
    
    one teacher can teach many streams and one stream can be taught by one teacher
    pizza can have many toppings and a topping can be in many pizzaz 
    eg{
        stream=models.ManyToManyField('streamTable')
        generally manyTomany instances should go in the object that is goin to be edited
        eg {
            streams will be editted in the teachers form 
        }  
    }    
    
}

"""