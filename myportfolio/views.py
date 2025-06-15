from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ProjectsSection
from .serializer import ProjectsSerializer

class ProjectsView(APIView):
    def get(self,request):
        projects= ProjectsSection.objects.all()
        serializer = ProjectsSerializer(projects,many=True)
        return Response (serializer.data)