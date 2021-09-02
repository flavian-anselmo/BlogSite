from django.contrib import admin
from myblogs.models import Post,Category
class PostAdmin(admin.ModelAdmin):
    pass
class CategoryAdmin(admin.ModelAdmin):
    pass

#this is how you register the models to the admin portal 
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)


# Register your models here.
"""
here is where i register my models so that 
class instances can be created usng django admiin
 for our case the admin part is the post and the category the post
 belongs 
 import mmodels you want to register to the django admin 
 
 comments are for the endusers to input 
 
 there is also a decorator for registering your modelAdmin
 @admin.register(Post)
 class post(author) :
    pass 
it gives onr or more model classes to register with ModelAdmin    
"""