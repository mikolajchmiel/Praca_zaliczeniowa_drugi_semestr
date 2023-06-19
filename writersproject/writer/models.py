from django.db import models


class Writer(models.Model):
    class WriterCountry(models.TextChoices):
        UNKNOWN = 'Unknown'
        FRANCE = 'France'
        POLAND = 'Poland'
        GERMANY = 'Germany'
        ENGLAND = 'England'
        USA = 'USA'
    name = models.CharField(blank=False, default='Unknown',
                            max_length=150, unique=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    year_of_death = models.IntegerField(blank=True, null=True)
    number_of_novels = models.IntegerField(blank=True, null=True)
    number_of_novellas = models.IntegerField(blank=True, null=True)
    number_of_volumes_of_poetry = models.IntegerField(blank=True, null=True)
    country_of_origin = models.CharField(blank=False,
                                         default=WriterCountry.UNKNOWN,
                                         max_length=25,
                                         choices=WriterCountry.choices)

    def __str__(self):
        return f'{self.id}: {self.name}'


