from rest_framework import serializers
from .models import Designation, Specialization, SkillSeeker 


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class SkillSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillSeeker
        fields = '__all__'
    
    def create(self, validated_data):
        image_url = validated_data.pop('image', None)
        company_logo_url = validated_data.pop('company_logo', None)

        skill_seeker = SkillSeeker.objects.create(**validated_data)
        if image_url and company_logo_url:
            skill_seeker.image = image_url
            skill_seeker.company_logo = company_logo_url
            skill_seeker.save()
        return skill_seeker      

