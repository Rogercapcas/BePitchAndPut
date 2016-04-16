from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player (models.Model):
    name = models.CharField(max_length=100)
    number_of_player = models.IntegerField()
    birthdate = models.DateField(default=date.today)
    stateOrProvince = models.TextField(blank=True, null=True)
    city = models.TextField()
    street = models.TextField(blank=True, null=True)
    zipCode = models.TextField(blank=True, null=True)
    telephone = models.IntegerField()
    handicap = models.FloatField()

    def __unicode__(self):
        return u"%s%" % Player.number_of_player

class Field(models.Model):
    city = models.CharField(max_length=100)
    holes = models.IntegerField()
    par = models.IntegerField()


class Hole (models.Model):
    field = models.ForeignKey(Field)
    hole_number = models.IntegerField()
    meters = models.IntegerField()
    handicap_hole = models.IntegerField()


class Match (models.Model):
    hole = models.ForeignKey(Hole)
    hole_result = models.IntegerField()

class Result (models.Model):
    match = models.ForeignKey(Match)
    match_result = models.IntegerField()
    handicap_variation = models.FloatField()

    def __unicode__(self):
        return u"$s%" % Result.match

    def get_match_result (self):
        return u"%s%" % Result.match_result


class Rule (models.Model):
    rules = models.TextField()

    def __unicode__(self):
        return u"%s%" % self.rules

class WeatherConditions (models.Model):
    windSpeed = models.IntegerField()
    windDirection = models.TextField()
