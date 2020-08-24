import pytest

from cars_app.models import Car, Rating


def create_cars():
    Car.objects.create(make="Honda", model="Accord")
    Car.objects.create(make="Audi", model="A6")
    Car.objects.create(make="Opel", model="Corsa")


@pytest.mark.django_db
def test_car_create():
    create_cars()
    assert Car.objects.count() == 3


@pytest.mark.django_db
def test_rating_create():
    create_cars()
    cars = Car.objects.all()
    Rating.objects.create(rate=3, car=cars[0])
    Rating.objects.create(rate=5, car=cars[1])
    assert Rating.objects.count() == 2
