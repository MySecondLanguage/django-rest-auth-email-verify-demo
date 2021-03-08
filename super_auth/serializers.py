
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError

from super_auth.models import User

from rest_auth.registration.serializers import RegisterSerializer

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = User
        fields = ('pk', 'email', 'full_name')
        read_only_fields = ('email', )


class CustomRegisterSerializer(RegisterSerializer):
    # inheriated from https://github.com/Tivix/django-rest-auth/blob/master/rest_auth/registration/serializers.py
    username = None
    # full_name = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=True)