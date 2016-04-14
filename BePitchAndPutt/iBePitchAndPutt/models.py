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
    player = models.ForeignKey(Player)
    date = models.DateTimeField()
    hole = models.ForeignKey(Hole)
    hole_result = models.IntegerField()
    weather = models.ForeignKey

    def getMatchResult(mn):
        return ModelName.objects.filter(self.match_number==mn).aggregate(Sum('hole_result'))

    def __unicode__(self):
        return u'%s' % self.match_number

class Rule (models.Model):
    rules = models.TextField()
