from rest_framework import serializers
from .models import SkillCrafter, ProjectProposal, Review 


class SkillCrafterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCrafter
        fields = '__all__'
    
    def create(self, validated_data):
        image_url = validated_data.pop('image', None) 

        skill_crafter = SkillCrafter.objects.create(**validated_data)
        if image_url:
            skill_crafter.image = image_url 
            skill_crafter.save()
        return skill_crafter     


class ProjectProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProposal
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

