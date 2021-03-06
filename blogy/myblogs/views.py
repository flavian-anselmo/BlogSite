from myblogs.models import Category, Post,Comment
from django.shortcuts import render
from django.http import HttpResponse, request#import thr httpresposnse 
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
    #THE  variable category will be passed in the urls patterns 
    #to fetch the re spective category 
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
                comment=form.cleaned_data['body'],
                post=post
            )
            #save the comment that hase been ceated 
            comment.save()
            print('saved')
        else:
            #get the errors generated 
            print('not ok ')
            print(form.errors)    
         
    comments=Comment.objects.filter(post=post) 
    context={
		"post":post,
		"comments":comments,
        "form":form,
  
	}	  
    #render the ui as per the  data provided in the dictionary 
    return render(request,"blogdetail.html",context)

def see_requests(self):
    text=f"""
    some text attributes of the httprequest object::
    scheme:{request.scheme}
    path:{request.path}
    method{request.method}
    GET:{request.GET}
    user:{request.user}
    """
    return HttpResponse(text,content_type="text/plain")



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