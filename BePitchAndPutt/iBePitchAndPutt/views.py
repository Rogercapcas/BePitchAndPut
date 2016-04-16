from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template


from django.contrib.auth.models import User
from django.utils import timezone

from .models import Player, Field, Hole, Match, Result, Rule, WeatherConditions
# Create your views here.
<<<<<<< HEAD

def mainpage(request):
    return render_to_response(

    'mainpage.html',
    {
        'titlehead': 'BePitchAndPutt app',
        'pagetitle': 'Welcome to BePitchAndPutt app',
        'contentbody': 'Your best application to see your training results',
        'user': request.user
    })

def results(request):
    return render_to_response(

    'results.html',
    {
        'titlehead': 'Results for ' request.user,
        'pagetitle': 'On ': request.results.match.date + ' at ' + request.results.match_h
        'contentbody': 'Result:' + request.results.match_result + '. Handicap variation:' + request.results.handicap_variation
    })

def weather(request):
    return render_to_response(

    'weather.html',
    {



    })

def stadistics(request):
    return render_to_response(

    'stadistics.html',
    {


    })
=======
>>>>>>> 844833facfeb38c9b7ac79b76eaca1c5a4480a3c
