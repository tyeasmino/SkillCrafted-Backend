from django.shortcuts import render
from rest_framework.views import APIView
from .models import ProjectCategory, Project
from .serializers import ProjectCategorySerializer, ProjectSerializer
from rest_framework.response import Response
from rest_framework import status 
from django.http import Http404
from .permissions import IsSkillSeekerOrReadOnly

# Create your views here.
class ProjectCategoryList(APIView):
    def get(self,request): 
        projectCategories = ProjectCategory.objects.all()
        serializer = ProjectCategorySerializer(projectCategories, many=True)
        return Response(serializer.data)

    def post(self,request): 
        serializer = ProjectCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectCategoryDetails(APIView):
    def get_object(self, pk):
        try: 
            return ProjectCategory.objects.get(pk=pk)
        except ProjectCategory.DoesNotExist:
            raise HTTP_404

    def get(self,request,pk, format=None): 
        category = self.get_object(pk) 
        serializer = ProjectCategorySerializer(category)
        return Response(serializer.data)

    def put(self,request,pk, format=None): 
        category = self.get_object(pk) 
        serializer = ProjectCategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk, format=None): 
        category = self.get_object(pk)  
        category.delete()
 
        return Response(status=status.HTTP_204_NO_CONTENT)  


class ProjectList(APIView):
    def get(self,request, format=None): 
        queryset = Project.objects.all()
        skill_seeker_id = request.query_params.get('skillSeeker')
        print(skill_seeker_id)

        if skill_seeker_id is not None:
            queryset = queryset.filter(skillSeeker__id = skill_seeker_id)


        category_slug = request.query_params.get('categorySlug')
        if category_slug:
            # Filter by category slug
            category = ProjectCategory.objects.filter(slug=category_slug).first()
            if category:
                queryset = queryset.filter(category=category)
            else:
                return Response({"detail": "Category not found."}, status=status.HTTP_404_NOT_FOUND)
        

        min_budget = request.query_params.get('budget__gte')
        max_budget = request.query_params.get('budget__lte')

        if min_budget:
            queryset = queryset.filter(budget__gte=min_budget)
        if max_budget:
            queryset = queryset.filter(budget__lte=max_budget)

        if min_budget and max_budget:
            queryset = queryset.filter(budget__gte=min_budget, budget__lte=max_budget)


        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format=None): 
        permission_classes = [IsSkillSeekerOrReadOnly]
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(skillSeeker = request.user.skillseeker)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProjectDetails(APIView):
    def get_object(self, pk):
        try: 
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self,request,pk, format=None):
        project = self.get_object(pk) 
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        project = self.get_object(pk) 
        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk, format=None):
        project = self.get_object(pk)  
        project.delete()
 
        return Response(status=status.HTTP_204_NO_CONTENT)  

