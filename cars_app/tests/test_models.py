import pytest

from cars_app.models import Car, Rating



def create_cars():
    Car.objects.create(make="Honda", model="Accord")
    Car.objects.create(make="Audi", model="A6")
    Car.objects.create(make="Opel", model="Corsa")


@pytest.mark.django_db
def test_book_create():
    create_cars()
    assert Car.objects.count() == 3

#
# @pytest.mark.django_db
# def test_author_create():
#     Author.objects.get_or_create(name=faker.name())
#     assert Author.objects.count() == 1
#
#
# @pytest.mark.django_db
# def test_category_create():
#     Category.objects.get_or_create(name=faker.file_name())
#     assert Category.objects.count() == 1