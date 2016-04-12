from django.db import models

# Create your models here.

class Player (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    handicap = models.FloatField()

class Match (models.Model):

    hole = models.ForeignKey(Hole)
    hole_result = models.IntegerField()
    total_result = models.IntegerField()

class Hole (models.Model):
    field = models.ForeignKey(Field)
    hole_number = models.IntegerField()
    meters = models.IntegerField()
    handicap_hole = IntegerField()


class Field(models.Model):
    holes = models.IntegerField()
    par = models.IntegerField()
