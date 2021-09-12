from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'age', 'avatar', 'phone_number', 'bio')
        extra_kwargs = {
            'user': {'required': False}
        }


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email'),
        )

        profile_data = validated_data.pop('profile')
        Profile.objects.create(
            user=user,
            age=profile_data['age'],
            phone_number=profile_data['phone_number'],
        )

        return user

    def to_representation(self, instance):
        request = self.context['request']
        Token.objects.get_or_create(user=instance)
        data = super(UserSerializer, self).to_representation(instance)
        if request.user == instance:
            data['token'] = instance.auth_token.key
        return data
