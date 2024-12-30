from django.contrib import admin
from .models import Project, ProjectCategory


class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

# Register your models here.
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Project)