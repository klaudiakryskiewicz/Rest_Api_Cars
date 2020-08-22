import pytest
from django.urls import reverse

from cars_app.models import Car



@pytest.mark.django_db
def test_cars_view(client):
    url = reverse("cars")
    response = client.get(url)
    assert response.status_code == 200

#
# @pytest.mark.django_db
# def test_book_detail(client):
#     book = create_book()[0]
#     url = reverse('details', kwargs={'id': book.id})
#     response = client.get(url)
#     assert response.status_code == 200
#
#
# @pytest.mark.django_db
# def test_unknown_book_detail(client):
#     url = reverse('details', kwargs={'id': 100})
#     response = client.get(url)
#     assert response.status_code == 404
#
#
# @pytest.mark.django_db
# def test_import_database(client):
#     for i in range(10):
#         create_book()
#     first_book_before = Book.objects.first()
#     response = client.post(reverse("import"), {"q": "war"})
#     assert response.status_code == 200
#     assert Book.objects.count() == 10
#     assert not Book.objects.first().title == first_book_before.title