from django.db import models
from musician.models import Musician
from django.core.validators import MaxValueValidator, MinValueValidator

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.album_name
