from rest_framework import serializers
from users.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = AppUser
        fields = ('id','username','first_name', 'last_name', 'is_active', 'gender')