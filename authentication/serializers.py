from authentication.models import User, SystemAdmin, Driver, Passenger, FleetManager
from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin


class UserSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = User
        fields = '__all__'
        lookup_field = 'id'


class SystemAdminSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = SystemAdmin
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = Driver
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = Passenger
        fields = '__all__'


class FleetManagerSerializer(serializers.ModelSerializer, FriendlyErrorMessagesMixin):
    class Meta:
        model = FleetManager
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
