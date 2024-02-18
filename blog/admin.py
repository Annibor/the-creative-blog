"""
Registering models with the Django admin interface.

"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on')
    list_filter = ('status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = ('title')
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Category)
admin.site.register(Comment)
