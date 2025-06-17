from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProjectsSection,SkillLists
from .serializer import ProjectsSerializer,SkillsListSerializer

class ProjectsView(APIView):
    def get(self,request):
        projects= ProjectsSection.objects.all()
        serializer = ProjectsSerializer(projects,many=True)
        return Response (serializer.data)
class SkillsView(APIView):
    def get(self,request):
        skills = SkillLists.objects.all()
        serializer2=SkillsListSerializer(skills,many=True)
        return Response(serializer2.data)
    