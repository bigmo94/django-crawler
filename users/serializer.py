import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from .models import Profile
from .utils import send_verification_code


def generate_code():
    return random.randint(10000, 99999)


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


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)

    def create(self, validated_data):
        email = validated_data['email']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = User.objects.create_user(
                username=validated_data.get('username'),
                password=validated_data.get('password'),
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
                email=validated_data.get('email'),
            )

        verify_code = generate_code()
        cache_key = 'login_code_{}'.format(email)
        cache.set(cache_key, verify_code, timeout=120)

        send_verification_code(user.email, verify_code)

        return user


class ObtainTokenSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('email', 'password', 'token')

    def create(self, validated_data):
        user = authenticate(**validated_data)

        if not user:
            raise ValidationError('Wrong credentials sent')

        Token.objects.get_or_create(user=user)

        return user

    def get_token(self, obj):
        return obj.auth_token.key
