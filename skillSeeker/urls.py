from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'designation', views.DesignationViewSet)
router.register(r'specialization', views.SpecializationViewSet)
router.register(r'skill-seekers', views.SkillSeekerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
