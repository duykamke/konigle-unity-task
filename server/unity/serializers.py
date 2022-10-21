from django.core.validators import validate_email
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def validate_email(self, data):
        validate_email(data)
        return

    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["subscription_status"] = instance.get_subscription_status_display()
        return response
