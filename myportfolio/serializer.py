from .models import ProjectsSection
from rest_framework import serializers

class ProjectsSerializer (serializers.ModelSerializer):
    class Meta:
        model =ProjectsSection
        fields= '__all__'