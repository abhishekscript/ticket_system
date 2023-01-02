from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model."""

    User._meta.get_field('email')._unique = True
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'password'
        )
        extra_kwargs = {
            'username': {'required': False},
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password =  validated_data.pop('password')
        user = User(**validated_data)
        user.username = validated_data['email']
        user.set_password(password)
        user.save()
        return user
