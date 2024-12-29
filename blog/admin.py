from django.contrib import admin
from .models import Blog,Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'published_date']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment,CommentAdmin)