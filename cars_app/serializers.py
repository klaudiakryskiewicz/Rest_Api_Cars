from rest_framework import serializers

from .models import Car


class CarSerializer(serializers.ModelSerializer):
    """
    Serializer for Car model
    """

   # no_of_rates = serializers.IntegerField(source='no_of_rates')
    average_rate = serializers.FloatField

    class Meta:
        model = Car
        fields = ['make', 'model', 'average_rate']


class CarAddSerializer(serializers.ModelSerializer):
    """
    Serializer for Car model
    """

    class Meta:
        model = Car
        fields = '__all__'