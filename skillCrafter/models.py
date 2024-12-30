from django.db import models 
from skillSeeker.models import Specialization
from skillSeeker.models import SkillSeeker
from projects.models import Project
from django.contrib.auth.models import User

# Create your models here.
class SkillCrafter(models.Model):
    # personal details 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(max_length=255, blank=True, null=True)
    curriculum_vitae = models.URLField(max_length=255, blank=True, null=True)
    specialization = models.ManyToManyField(Specialization) 

    # educational details 
    last_educational_qualification = models.CharField(max_length=50, blank=True, null=True)
    last_educational_institution = models.CharField(max_length=50, blank=True, null=True)
    last_passing_year = models.DateField(blank=True, null=True) 
    last_result = models.CharField(max_length=4, blank=True, null=True)

    # job experience details 
    last_working_company = models.CharField(max_length=50, blank=True, null=True)
    last_working_years = models.CharField(max_length=50, blank=True, null=True)
    last_working_projects_link_1  = models.URLField(blank=True, null=True)
    last_working_projects_link_2  = models.URLField(blank=True, null=True) 

    # contact details 
    whatsapp = models.CharField(max_length=11,blank=True, null=True)
    linkedin = models.URLField(max_length=100,blank=True, null=True)
    github = models.URLField(max_length=100,blank=True, null=True)
    portfolio = models.URLField(max_length=100,blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



PROGRESS_CHOICES = [ 
    ('2', 'Not Started'), 
    ('1', 'Yes'), 
    ('0', 'No'), 
]



class ProjectProposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    proposed_by = models.ForeignKey(SkillCrafter, on_delete=models.CASCADE)
    proposal = models.TextField()
    is_proposal_accepted = models.BooleanField(default=False)
    is_completed = models.CharField(max_length=1, choices=PROGRESS_CHOICES, default='2')

    def __str__(self):
        return f'{self.project.title} - {self.proposed_by}'
    


STAR_CHOICES = [
    ('★☆☆☆☆', '★☆☆☆☆'),
    ('★★☆☆☆', '★★☆☆☆'),
    ('★★★☆☆', '★★★☆☆'),
    ('★★★★☆', '★★★★☆'),
    ('★★★★★', '★★★★★'),
]


class Review(models.Model):
    completed_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(SkillSeeker, on_delete=models.CASCADE)
    skillCrafter = models.ForeignKey(SkillCrafter, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=STAR_CHOICES, max_length=10) 

    def __str__(self):
        return f"{self.reviewer.user.first_name} reviewed for: {self.skillCrafter.user.first_name}, for: {self.completed_project.title}"

