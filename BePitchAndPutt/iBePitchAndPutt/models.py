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
    name = models.CharField(max_length=100, blank=False)
    number_of_player = models.AutoField(primary_key=True, unique=True)
    birthdate = models.DateField()
    country = models.CharField(max_length=100)
    stateOrProvince = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100,blank=True, null=True)
    zipCode = models.CharField(max_length=100,blank=True, null=True)
    telephone = models.IntegerField(null = False, blank = False)
    handicap = models.FloatField(null = True, blank = True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u'%s' % self.name
    def get_absolute_url(self):
        return reverse('PlayerDetail',kwargs={'pk':self.pk})


class Field(models.Model):
    FieldCode = models.IntegerField(null = False, blank = False)
    field_name = models.CharField(blank = False, null = False, max_length=100)
    stateOrProvince = models.CharField(max_length=100,blank=True, null=True)
    city = models.CharField(null = False, blank = False, max_length=100)
    street = models.CharField(max_length=100,blank=True, null=True)
    zipCode = models.CharField(max_length=100,blank=True, null=True)
    telephone = models.IntegerField(null = True, blank = True)
    url = models.URLField(blank=True, null=True)
    number_of_holes = models.IntegerField()
    par = models.IntegerField(null = False, blank = False)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u'%s' % self.field_name

class Hole (models.Model):
    field = models.ForeignKey(Field, null=False, related_name='holes')
    hole_number = models.IntegerField(null = False, blank = False)
    meters = models.IntegerField(null = False, blank = False)
    handicap_hole = models.IntegerField(null = False, blank = False)
    user = models.ForeignKey(User, default=1)
    def __unicode__(self):
        return u'%i' % self.hole_number

class WeatherConditions (models.Model):
    date = models.CharField(max_length=100,default='today')
    windSpeed = models.FloatField()
    windDirection = models.TextField()
    user = models.ForeignKey(User, default=1)

class Match (models.Model):
    match_number = models.AutoField(primary_key=True, unique=True)
    player = models.ForeignKey(Player,null=True, related_name='matches')
    date = models.DateTimeField()
    weather = models.ForeignKey(WeatherConditions, null = True, blank = True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u'%i' % self.match_number

class Throw (models.Model):
    hole = models.ForeignKey(Hole,null=True, related_name='throws')
    match = models.ForeignKey(Match,null=True, related_name='throws')
    score = models.IntegerField( null = False, blank = False)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u'Hole: %s, Match: %s, Score: %i' % (self.hole, self.match,self.score)

