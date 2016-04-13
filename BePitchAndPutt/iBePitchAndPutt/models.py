from	django.db	import	models
from	datetime	import	date
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Player (models.Model):
    name = models.ForeignKey('auth.User')
    number_of_player = models.IntegerField()
    birthdate = models.DateField()
    stateOrProvince = models.TextField(blank=True, null=True)
    city = models.TextField(max_length=100)
    street = models.TextField(blank=True, null=True)
    zipCode = models.TextField(blank=True, null=True)
    telephone = models.IntegerField()
    handicap = models.FloatField()

    def __unicode__(self):
        return u"%s%" % Player.number_of_player

class Field(models.Model):
    fieldCode = models.IntegerField()
    stateOrProvince = models.TextField(blank=True, null=True)
    city = models.TextField(max_length=100)
    street = models.TextField(blank=True, null=True)
    zipCode = models.TextField(blank=True, null=True)
    telephone = models.IntegerField()
    url = models.URLField(blank=True, null=True)
    number_of_holes = models.IntegerField()
    par = models.IntegerField()

<<<<<<< HEAD
=======
    def __unicode__(self):
        return u"%s%" % Field.FieldCode


>>>>>>> 66f03387742cf4bc25c0a5dad0929bd1b9cc0d98
class Hole (models.Model):
    field = models.ForeignKey(Field)
    hole_number = models.IntegerField()
    meters = models.IntegerField()
    handicap_hole = models.IntegerField()

    def __unicode__(self):
        return u"%s%" % Hole.hole_number

class Match (models.Model):
    match_number = models.IntegerField()
    match_h = models.TextField()
    hole = models.ForeignKey(Hole)
    hole_result = models.IntegerField()
    weather = models.ForeignKey

    def __unicode__(self):
        return u"%s%" % Match.match_number
class Result (models.Model):
    match = models.ForeignKey(Match)
    match_result = models.IntegerField()
    handicap_variation = models.FloatField()
    date = models.DateTimeField(default=timezone.now)


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
    Wind = windSpeed + "" + windDirection

    def __unicode__(self):
        return u"%s%" % WeatherConditions.Wind
