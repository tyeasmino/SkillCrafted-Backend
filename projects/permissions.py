from rest_framework import permissions

class IsSkillSeekerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated 
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.skillSeeker.user == request.user 


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_superuser)


class IsSkillCrafterUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and not request.user.is_staff 

 
class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user or not request.user.is_authenticated
    
