from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import SkillCrafter, ProjectProposal, Review
from .serializers import SkillCrafterSerializer, ProjectProposalSerializer, ReviewSerializer


# Create your views here.
class SkillCrafterViewSet(viewsets.ModelViewSet):
    queryset = SkillCrafter.objects.all()
    serializer_class = SkillCrafterSerializer 


class ProjectProposalViewSet(viewsets.ModelViewSet):
    queryset = ProjectProposal.objects.all()
    serializer_class = ProjectProposalSerializer

 
class ProjectProposalList(generics.ListAPIView):
    serializer_class = ProjectProposalSerializer

    def get_queryset(self):
        queryset = ProjectProposal.objects.all()
        proposed_by = self.request.query_params.get('proposed_by')  # User ID (i.e., SkillCrafter ID)
        project_id = self.request.query_params.get('project')  # Project ID

        # Filter by proposed_by and project_id if they exist
        if proposed_by is not None:
            queryset = queryset.filter(proposed_by__id=proposed_by)
        
        if project_id is not None:
            queryset = queryset.filter(project__id=project_id)

        return queryset



class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()
        skill_crafter_id = self.request.query_params.get('skillCrafter')

        if skill_crafter_id is not None:
            queryset = queryset.filter(skillCrafter__id = skill_crafter_id)
        
        return queryset
        

