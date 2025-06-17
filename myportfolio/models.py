from django.db import models

# Create your models here.


class ProjectsSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.JSONField()
    image_url = models.URLField(blank=True, null=True)
    icons = models.CharField(max_length=200)
    github_Url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Project name = {self.title}'


class SkillLists(models.Model):
    skill_title = models.CharField(max_length=200)
    icons_url=models.URLField(blank=True,null=True)
    skills = models.JSONField()

    def __str__(self):
        return f'{self.skill_title}-Skills'
