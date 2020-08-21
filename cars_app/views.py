from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from cars_app.models import Car
from cars_app.serializers import CarSerializer


class CarsView(APIView):
    """
    """

    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request):
        pass
