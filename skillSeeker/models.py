from django.db import models 
from django.contrib.auth.models import User

# Create your models here.  
class Designation(models.Model):
    name = models.CharField(max_length=30)          # HR, Manager etc
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name
    

class Specialization(models.Model):
    name = models.CharField(max_length=30)          # web development, cyber specialist etc 
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name
        

class SkillSeeker(models.Model):
    # personal details 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(max_length=255, blank=True, null=True)
    designation = models.ManyToManyField(Designation)   
    specialization = models.ManyToManyField(Specialization) 

    # company details
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_started = models.CharField(max_length=20,  blank=True, null=True)
    company_employee = models.IntegerField(blank=True, null=True)
    company_address = models.CharField(max_length=200, blank=True, null=True)
    company_website = models.CharField(max_length=100, blank=True, null=True)
    company_logo = models.URLField(max_length=255, blank=True, null=True)

    # contact details 
    whatsapp = models.CharField(max_length=11, null=True, blank=True)
    linkedin = models.CharField(max_length=50, null=True, blank=True)
    github = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


