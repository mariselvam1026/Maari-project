from django.contrib import admin
from .models import Post,Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
  
admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

# @admin.register(SubComment)
# class SubCommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email','replycomment', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')


