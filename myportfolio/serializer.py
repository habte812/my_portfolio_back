from .models import ProjectsSection,SkillLists
from rest_framework import serializers

class ProjectsSerializer (serializers.ModelSerializer):
    class Meta:
        model =ProjectsSection
        fields= '__all__'
        
class SkillsListSerializer(serializers.ModelSerializer):
    class Meta:
        model= SkillLists
        fields='__all__'