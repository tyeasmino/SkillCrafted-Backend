from django.contrib.auth.models import User
from django.db import models
from skillSeeker.models import SkillSeeker

# Create your models here.
class ProjectCategory(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50)
    icon = models.CharField(max_length=20, blank=True, null=True)
    services_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Project(models.Model):
    title = models.CharField(max_length=100)
    skillSeeker = models.ForeignKey(SkillSeeker, on_delete=models.CASCADE)
    description = models.TextField()
    budget = models.IntegerField()
    deadline = models.DateField()
    requirements = models.TextField(blank=True, null=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    anyAttachment = models.URLField(max_length=255, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f'{self.title} - {self.skillSeeker}'  
    