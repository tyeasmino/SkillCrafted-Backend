from rest_framework import serializers
from .models import ProjectCategory, Project

class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
    
    def create(self, validated_data):
        attachement_url = validated_data.pop('anyAttachment', None)
        project = Project.objects.create(**validated_data)
        if attachement_url:
            project.anyAttachment = attachement_url     
            project.save()
        return project



