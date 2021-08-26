from django import forms
from django.forms import widgets
#this is where forms are created 
class CommentForm(forms.Form):
    #if i inherit form forms i have to declare the fields here unlike model forms 
    #model forms use class mets
    #text fields do not work use charfields 
    author=forms.CharField(max_length=100,
                           #one must input his or her name 
                           required=True,
                           widget=forms.TextInput(attrs={
							   "class":"form-control",
								"placeholder":"your name",			
          
						   })
                           )
    body=forms.CharField(max_length=100,widget=forms.Textarea(attrs={
		"class":"form-control",
  		"placeholder":"Leave a comment",
	}))
    
"""
the attributes added in the widgets are based on the html tags 
eg class 
row 
column 
placeholder
etc 
the widgets allow as to specify some css classes which will help in formatting the 
teplate for this view later and also allow as to add some place holder text 


when a form is posted a POST request is sent to the server there fore in the view 
function we need to check if the POST request as bee sent and after that a comment can be created 
check if the form fields have been field correctly with the is_valid methos 

once the comment is created we need to save it 
"""    