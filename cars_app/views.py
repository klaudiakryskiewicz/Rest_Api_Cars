import json
import urllib.request

from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import mixins, generics
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView, ListAPIView

from cars_app.models import Car, Rating
from cars_app.serializers import CarSerializer, RatingSerializer, CarPopularSerializer


class CarsView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    API displaying a list of all cars,
    allowing to add a new car if car exists in an external database
    """
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


class RateView(CreateAPIView):
    """
    API allowing to rate a car
    """
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()


class CarsPopularView(ListAPIView):
    """
    API displaying five cars with the biggest number of rates
    """
    queryset = Car.objects.all().annotate(rate_count=Count('ratings')).order_by('-rate_count')[:5]
    serializer_class = CarPopularSerializer
