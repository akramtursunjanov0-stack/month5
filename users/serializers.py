from rest_framework import serializers
from django.contrib.auth.models import User 
from rest_framework.exceptions import ValidationError


class RegisterSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField()


    def validate_name(self, username ):
        try:
            User.objects.get(username=username)
        except User .DoesNotExist:
            return username
        raise ValidationError('ПОЛЬЗВАЛЕТЬ УЖЕ СУЩЕСТВУЕТ !')