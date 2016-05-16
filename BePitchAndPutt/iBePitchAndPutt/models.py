from	django.db	import	models
from	datetime	import	date
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Sum
import sys
import requests
import json
# Create your models here.

class Player (models.Model):
    name = models.CharField(max_length=100)
    number_of_player = models.IntegerField()
    birthdate = models.DateField()
    stateOrProvince = models.TextField(blank=True, null=True)
    city = models.TextField(max_length=100)
    street = models.TextField(blank=True, null=True)
    zipCode = models.TextField(blank=True, null=True)
    telephone = models.IntegerField()
    handicap = models.FloatField()

    def __unicode__(self):
        return u'%s' % self.name
    def get_absolute_url(self):
        return reverse('PlayerDetail',kwargs={'pk':self.pk})


class Field(models.Model):
    FieldCode = models.IntegerField()
    field_name = models.CharField(max_length=100)
    stateOrProvince = models.TextField(blank=True, null=True)
    city = models.TextField(max_length=100)
    street = models.TextField(blank=True, null=True)
    zipCode = models.TextField(blank=True, null=True)
    telephone = models.IntegerField()
    url = models.URLField(blank=True, null=True)
    number_of_holes = models.IntegerField()
    par = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.field_name

class Hole (models.Model):
    field = models.ForeignKey(Field)
    hole_number = models.IntegerField(default=date.today)
    meters = models.IntegerField()
    handicap_hole = models.IntegerField()
    def __unicode__(self):
        return u'%i' % self.hole_number

class Match (models.Model):
    match_number = models.IntegerField()
    player = models.ForeignKey(Player,null=True, related_name='matches')
    date = models.DateTimeField()
    weather = models.ForeignKey

    def __unicode__(self):
        return u'%i' % self.match_number

class Throw (models.Model):
    hole = models.ForeignKey(Hole,null=True, related_name='throws')
    match = models.ForeignKey(Match,null=True, related_name='throws')
    score = models.IntegerField()

    def __unicode__(self):
        return u'%i%i' % (self.hole, self.match,)


class WeatherConditions (models.Model):
    date = models.TextField(default='today')
    windSpeed = models.FloatField()
    windDirection = models.TextField()
