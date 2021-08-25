from myblogs.models import Category, Post,Comment
from django.shortcuts import render
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
    posts=Post.objects.filter(categories__contains=category).order_by('-createdOn')
    #__contains to filter the categories 
    #order_by for ordering with the date they were created 
    context={
        "category":category,
		"posts":posts,
	}
    return render(request,"category.html",context)


def fetchByPrimarykey(request,pk):
    post=Post.objects.get(pk=pk) 
    comments=Comment.objects.filter(post=post) 
    context={
		"post":post,
		"comments":comments
  
	}	  
    return render(request,"detail.html",context)

# Create your views here.
"""
the app will have three views
index.html to display the list of all the posts in my blog site
detail.html to display the contents of the blog
category.html to display posts as per the category specified

use a - sign to specify the largest value since we want the most recent time     
"""