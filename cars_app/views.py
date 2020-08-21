import json
import urllib.request

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework import mixins, generics, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from cars_app.models import Car
from cars_app.serializers import CarSerializer


class CarsView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request):
        return self.list(self, request)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        make = serializer.data["make"]
        model = serializer.data["model"]

        if Car.objects.filter(make=make, model=model).first():
            raise APIException("This car already exists in database")

        with urllib.request.urlopen(
                f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json") as url:
            data = json.loads(url.read().decode())
            for car in data["Results"]:
                if car["Model_Name"] == model:
                    Car.objects.create(make=make, model=model)

                    return HttpResponseRedirect(reverse('cars'))
        raise APIException("This car doesn't exist!")
