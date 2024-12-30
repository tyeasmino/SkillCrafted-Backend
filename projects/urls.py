from django.urls import path, include
from .views import ProjectList, ProjectDetails, ProjectCategoryList, ProjectCategoryDetails


urlpatterns = [
    path('categoryList/', ProjectCategoryList.as_view(), name="category_list"),
    path('categoryList/<int:pk>/', ProjectCategoryDetails.as_view(), name="category_details"),

    path('projectList/', ProjectList.as_view(), name="project_list"),
    path('projectList/<int:pk>/', ProjectDetails.as_view(), name="project_details"),
]
