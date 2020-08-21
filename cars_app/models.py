from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum


class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def ratings(self):
        return Rating.objects.filter(car=self).count()

    def average_rate(self):
        return Rating.objects.aggregate(Sum('rate'))['rate']/self.ratings()

class Rating(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(5)])

    class Meta:
        verbose_name_plural = "ratings"