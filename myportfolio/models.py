from django.db import models

# Create your models here.

class ProjectsSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.JSONField()
    image_url =models.URLField(blank=True,null=True)
    icons =models.CharField(max_length=200)
    github_Url =models.URLField(blank=True,null=True)
    
class Skills(models.Model):
    title= models.CharField(max_length=200)
    skill_lists=models.JSONField(blank=True,null=True)
    