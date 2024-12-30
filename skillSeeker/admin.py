from django.contrib import admin
from .models import Specialization, Designation, SkillSeeker

# Register your models here.
class SpecializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}




admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(SkillSeeker)