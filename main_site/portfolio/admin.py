from django.contrib import admin
from .models import Project, Photo


# define how photos appear in project
class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1
    fields = ("image", "caption", "order")
    ordering = ("order",)


# define how projects appear in admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    search_fields = ("title", "category")
    list_filter = ("category",)
    fields = ("title", "description", "category", "url", "image")
    inlines = [PhotoInline]  # referecnces photos above


# view and edit photos separately
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("project", "order", "id")
    ordering = ("project", "order")
