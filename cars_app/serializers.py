from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model
    """

    class Meta:
        model = Car
        fields = '__all__'
