from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Avg


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def no_of_rates(self):
        return Rating.objects.filter(car=self).count()

    def average_rate(self):
        if self.no_of_rates() == 0:
            return 0
        return Rating.objects.filter(car=self).aggregate(Avg('rate'))['rate__avg']

    def __str__(self):
        return f"{self.make} {self.model}"


class Rating(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])

    class Meta:
        verbose_name_plural = "ratings"
