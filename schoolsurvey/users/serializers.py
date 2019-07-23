from rest_framework import serializers
from .models import User,UserProfile

class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the token data
    """
    token = serializers.CharField(max_length=255)
    
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id","email","username","role")



# class SchoolProfileSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = SchoolProfile
#         fields = ('doo', 'address', 'county', 'zip', 'photo')


# class SchoolSerializer(serializers.HyperlinkedModelSerializer):
#     profile = SchoolProfileSerializer(required=True)

#     class Meta:
#         model = School
#         fields = ('url', 'email', 'username', 'password', 'profile')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         password = validated_data.pop('password')
#         school = School(**validated_data)
#         school.set_password(password)
#         school.save()
#         SchoolProfile.objects.create(school=school, **profile_data)
#         return school

#     def update(self, instance, validated_data):
#         profile_data = validated_data.pop('profile')
#         profile = instance.profile

#         instance.email = validated_data.get('email', instance.email)
#         instance.save()

#         profile.dob = profile_data.get('doo', profile.doo)
#         profile.address = profile_data.get('address', profile.address)
#         profile.county = profile_data.get('county', profile.county)
#         profile.zip = profile_data.get('zip', profile.zip)
#         profile.photo = profile_data.get('photo', profile.photo)
#         profile.save()

#         return instance