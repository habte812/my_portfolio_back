from django.db import models

# Create your models here.

class ProjectsSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.JSONField()
    colors =models.URLField(blank=True,null=True)
    icons =models.CharField(max_length=200)
    githubUrl =models.URLField(blank=True,null=True)