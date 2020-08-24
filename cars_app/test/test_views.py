import pytest
from django.urls import reverse

from cars_app.models import Car, Rating
from cars_app.test.test_models import create_cars


@pytest.mark.django_db
def test_car_view(client):
    create_cars()
    url = reverse("cars")
    response = client.get(url)
    assert len(response.data) == 3
    assert response.status_code == 200


@pytest.mark.django_db
def test_rate_view(client):
    url = reverse("rate")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_popular_view(client):
    url = reverse("popular")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_import_car(client):
    response = client.post(reverse("car"), {"make": "Audi", "model": "TT"})
    assert response.status_code == 200
    assert Car.objects.count() == 1


@pytest.mark.django_db
def test_import_wrong_car(client):
    response = client.post(reverse("car"), {"make": "Audi", "model": "A6"})
    assert response.status_code == 500
    assert Car.objects.count() == 0


@pytest.mark.django_db
def test_add_rate(client):
    create_cars()
    response = client.post(reverse("rate"), {"car": 1, "rate": 5})
    assert response.status_code == 200
    assert Rating.objects.count() == 1


@pytest.mark.django_db
def test_add_wrong_rate(client):
    create_cars()
    response = client.post(reverse("rate"), {"car": 1, "rate": 7})
    assert response.status_code == 400
    assert Rating.objects.count() == 0
