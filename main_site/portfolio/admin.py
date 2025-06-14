from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'category')
    list_filter = ('category',)
    fields = ('title', 'description', 'category', 'url', 'image') 