from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Designation, Specialization, SkillSeeker
from .serializers import DesignationSerializer, SpecializationSerializer, SkillSeekerSerializer


# Create your views here.
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer 


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class SkillSeekerViewSet(viewsets.ModelViewSet):
    queryset = SkillSeeker.objects.all()
    serializer_class = SkillSeekerSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return SkillSeeker.objects.filter(user = self.request.user)
    