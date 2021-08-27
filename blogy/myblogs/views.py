from myblogs.models import Category, Post,Comment
from django.shortcuts import render
from .forms import CommentForm #import thr form 
#this are functional views 
def fetchAllBlogs(request):
    posts=Post.objects.all().order_by('-createdOn')
    #order by the time the blog was created 
    context={
		"posts":posts,
	}
    #render the template in terms of the context
    return render(request,"index.html",context)

def fecthByCategory(request,category):
    #pass a category in the function
    posts=Post.objects.filter(categories__categoryName__contains=category).order_by('-createdOn')
    #__contains to filter the categories 
    #order_by for ordering with the date they were created 
    context={
        "category":category,
		"posts":posts,
	}
    return render(request,"category.html",context)


def fetchByPrimarykey(request,pk):
    post=Post.objects.get(pk=pk) #fetch data as per the primary key 
    form =CommentForm()#fetch an empty form and render it 
    if request.method=='POST':
        #create a comment instance 
        form =CommentForm(request.POST)#validates the form and post what the user enters 
        if form.is_valid():
            #if the entries are good 
            print(form.cleaned_data)
            comment=Comment(
                #a new instance of comment is created 
                #this is the table in the data base 
                #or our Comment model 
                #fetching the fields of the tbl in db and cleaning them 
                author=form.cleaned_data['author'],
                comment=form.cleaned_data['comment'],
                post=post
            )
            #save the comment that hase been ceated 
            comment.save()
        else:
            #get the errors generated 
            print(form.errors)    
         
    comments=Comment.objects.filter(post=post) 
    context={
		"post":post,
		"comments":comments,
        "form":form,
  
	}	  
    #render the ui as per the  data provided in the dictionary 
    return render(request,"blogdetail.html",context)





# Create your views here.
"""
the app will have three views
index.html to display the list of all the posts in my blog site
detail.html to display the contents of the blog
category.html to display posts as per the category specified

use a - sign to specify the largest value since we want the most recent time   


widgets in django is a representation of an html input element
the widget handles the rendering of the html and extraction of data
    
"""