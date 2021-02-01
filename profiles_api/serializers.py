from rest_framework import serializers
from profiles_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    '''serialize the user profile obj'''
    class Meta:
        model = models.UserProfile
        fields = ('id','name','email','password')
        #this is so that the password will not appear in the url and will be displayed with stars
        extra_kwargs = {
            'password': {
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    #override the default create method
    def create(self,validated_data):
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )
        return user
    
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on',)
        extra_kwargs = {
            'user_profile':{'read_only':True}
        }