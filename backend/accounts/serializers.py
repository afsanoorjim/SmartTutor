from rest_framework import serializers
from .models import Tutor


class RegisterTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        tutor = Tutor.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return tutor