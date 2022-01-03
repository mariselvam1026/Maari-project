from django.contrib import admin
from .models import post

class postAdmin(admin.ModelAdmin):
    list_display= ('title', 'body', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'body': ('title',)}

admin.site.register(post, postAdmin)

# Register your models here.
