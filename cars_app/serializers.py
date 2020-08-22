from rest_framework import serializers

from .models import Car, Rating


class CarSerializer(serializers.ModelSerializer):
    """
    Serializer for Car model
    """

    average_rate = serializers.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        model = Car
        fields = ['make', 'model', 'average_rate']


class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for Rating model
    """

    class Meta:
        model = Rating
        fields = ['car', 'rate']


class CarPopularSerializer(serializers.ModelSerializer):
    """
    Serializer for Car model
    """

    number_of_rates = serializers.IntegerField(source='no_of_rates')

    class Meta:
        model = Car
        fields = ['make', 'model', 'number_of_rates']


