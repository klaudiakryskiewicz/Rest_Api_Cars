from django.urls import reverse
from rest_framework.test import APITestCase

from cars_app.models import Car, Rating


class CarTest(APITestCase):
    def populate_db(self):
        car1 = Car.objects.create(make="Honda", model="Civic")
        car2 = Car.objects.create(make="Opel", model="Corsa")
        car3 = Car.objects.create(make="Audi", model="Q5")

        Rating.objects.create(rate=3, car=car1)
        Rating.objects.create(rate=5, car=car3)
        Rating.objects.create(rate=4, car=car3)


    def car_get_view(self):
        response = reverse('cars')

        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(response.data))

