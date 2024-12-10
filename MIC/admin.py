from django.contrib import admin
from .models import Blog
from .models import Comment
from .models import like

class Blogadmin(admin.ModelAdmin):
    list_display =['id', "title", "image", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "content"]

admin.site.register(Blog,Blogadmin)


class CommentAdmin(admin.ModelAdmin):
    list_display =['id', "content", "post", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["content"]

admin.site.register(Comment, CommentAdmin)

class likeAdmin(admin.ModelAdmin):
    list_display =['id', "like", "post", "created_at"]
    list_filter = ["created_at"]
    
admin.site.register(like, likeAdmin)
    

