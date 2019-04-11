from rest_framework import serializers 
from jogging.models import UserProfile, Record
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')
    def create(self, validate_data):
        

        user = User(
            username=validate_data['username'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name'],
        )
        user.set_password(validate_data['password'])
        user.save()
        UserProfile.objects.create(
            role = 'User',
            user = user
        )
        return user

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        depth = 2
        fields = ('id', 'date', 'distance', 'time','user', 'user_id')

        
