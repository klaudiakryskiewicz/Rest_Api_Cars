from django.urls import reverse

from rest_framework.test import APITestCase
from .models import Car, Rating


class ModelsTests(APITestCase):

    def test_create_cars(self):
        """Test saving cars to database"""
        Car.objects.create(make="Honda", model="Accord")
        Car.objects.create(make="Audi", model="A6")
        Car.objects.create(make="Opel", model="Corsa")
        self.assertEqual(Car.objects.count(), 3)

    def test_create_rating(self):
        """Test saving ratings to database"""
        car = Car.objects.create(make="Honda", model="Accord")
        Rating.objects.create(car=car, rate=3)
        self.assertEqual(Rating.objects.count(), 1)


class CarsViewTests(APITestCase):

    def test_list_cars(self):
        """Test displaying list of cars"""
        url = reverse('cars')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_add_car(self):
        """Test adding car with correct data"""
        response = self.client.post(reverse("cars"), {"make": "Audi", "model": "A6"})
        self.assertEqual(302, response.status_code)

    def test_add_invalid_car(self):
        """Test adding car with incorrect data"""
        response = self.client.post(reverse("cars"), {"make": "Opel", "model": "Astra"})
        self.assertEqual(500, response.status_code)

    def test_add_repeated_car(self):
        """Test adding car that already exists in database"""
        Car.objects.create(make="Audi", model="Q5")
        response = self.client.post(reverse("cars"), {"make": "Audi", "model": "Q5"})
        self.assertEqual(500, response.status_code)


class PopularViewTests(APITestCase):

    def test_popular_cars(self):
        """Test displaying list of cars"""
        url = reverse('popular')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_popular_order(self):
        """Test ordering cars based on number of rates"""
        car1 = Car.objects.create(make="Honda", model="Accord")
        car2 = Car.objects.create(make="Honda", model="Civic")
        car3 = Car.objects.create(make="Opel", model="Astra")

        Rating.objects.create(car=car1, rate=3)
        Rating.objects.create(car=car1, rate=5)
        Rating.objects.create(car=car3, rate=2)

        response = self.client.get(reverse("popular"))

        self.assertEqual(response.data['results'][0]['model'], car1.model)
        self.assertEqual(response.data['results'][1]['model'], car3.model)
        self.assertEqual(response.data['results'][2]['model'], car2.model)


class RateViewTests(APITestCase):
    def test_rate_cars(self):
        """Test displaying endpoint with incorrect method"""
        url = reverse('rate')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 405)

    def test_add_rate(self):
        """Test adding rate"""
        car = Car.objects.create(make="Audi", model="Q5")
        response = self.client.post(reverse("rate"), {"car": car.id, "rate": 5})
        self.assertEqual(201, response.status_code)

    def test_add_invalid_rate(self):
        """Test adding invalid rate"""
        car = Car.objects.create(make="Audi", model="Q5")
        response = self.client.post(reverse("rate"), {"car": car.id, "rate": 7})
        self.assertEqual(400, response.status_code)
