from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'skill-crafter', views.SkillCrafterViewSet, basename='skill-crafter')
router.register(r'project-proposal', views.ProjectProposalViewSet, basename='project-proposal')
router.register(r'project-review', views.ReviewViewSet, basename='project-review')

urlpatterns = [
    path('', include(router.urls)),
    path('filtered-project-proposals/', views.ProjectProposalList.as_view(), name="project_proposal_list")


# http://127.0.0.1:8000/skillCrafter/filtered-project-proposals/?project=2
# http://127.0.0.1:8000/skillCrafter/filtered-project-proposals/?proposed_by=3
# http://127.0.0.1:8000/skillCrafter/filtered-project-proposals/?project=2&proposed_by=3


]
