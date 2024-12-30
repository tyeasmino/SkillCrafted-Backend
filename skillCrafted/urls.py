from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('contact_us/', include("contactUs.urls")),
    path('projects/', include("projects.urls")),
    path('skillSeeker/', include("skillSeeker.urls")),
    path('skillCrafter/', include("skillCrafter.urls")),
    path('api-auth/', include("rest_framework.urls")),
    path('auth/', include("dj_rest_auth.urls")),
    path('auth/', include("django.contrib.auth.urls")), 
]
