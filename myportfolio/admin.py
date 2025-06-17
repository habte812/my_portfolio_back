from django.contrib import admin

# Register your models here.
from .models import ProjectsSection,SkillLists

admin.site.register(ProjectsSection)
admin.site.register(SkillLists)