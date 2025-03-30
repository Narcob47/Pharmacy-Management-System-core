from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'user_type', 
                 'plate_number', 'car_or_motor_photos', 'license_and_registration']
        extra_kwargs = {
            'password': {'write_only': True},
            'car_or_motor_photos': {'required': False},
            'license_and_registration': {'required': False},
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data['phone_number'],
            user_type=validated_data['user_type'],
        )
        
        if validated_data.get('plate_number'):
            user.plate_number = validated_data['plate_number']
        if validated_data.get('car_or_motor_photos'):
            user.car_or_motor_photos = validated_data['car_or_motor_photos']
        if validated_data.get('license_and_registration'):
            user.license_and_registration = validated_data['license_and_registration']
        
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type
        return token