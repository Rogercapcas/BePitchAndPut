from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template


from django.contrib.auth.models import User
from django.utils import timezone

from .models import Player, Field, Hole, Match, Result, Rule, WeatherConditions


def mainpage(request):
    return render_to_response(

    'mainpage.html',
    {
        'titlehead': 'BePitchAndPutt app',
        'pagetitle': 'Welcome to BePitchAndPutt app',
        'contentbody': 'Your best application to see your training results',
        'user': request.user
    })

def players(request):
    return render_to_response(

    'Player.html',
    {

    'titlehead' : "Players",
    'pagetitle' : "Players",
    'players': Player.objects.all(),
    })

def player_info(request,player_id):
    return render_to_response(

    'player_info.html',{

    'titlehead' : "Player info",
    'pegatitle' : "Player Information",
    'player': Player.objects.get(pk=player_id),

    })
