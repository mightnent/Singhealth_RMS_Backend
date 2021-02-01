from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    '''only allow user to edit their own profile'''
    def has_object_permission(self,request,view,obj):
        #if it is a http get
        if request.method in permissions.SAFE_METHODS:
            return True
        #only return true if the obj id is the same as the user request id,
        #this means that they are the same person
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id