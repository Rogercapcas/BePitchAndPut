from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template


from django.contrib.auth.models import User
from django.utils import timezone

from .models import Player, Field, Hole, Match, Result, Rule, WeatherConditions
# Create your views here.
