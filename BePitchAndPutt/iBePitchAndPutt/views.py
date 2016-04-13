from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template


from django.contrib.auth.models import User
from django.utils import timezone

from .models import Player, Field, Hole, Match,Rule, WeatherConditions


def mainpage(request):
    return render_to_response(

    'mainpage.html',
    {
        'titlehead': 'BePitchAndPutt app',
        'pagetitle': 'Welcome to BePitchAndPutt app',
        'contentbody': 'Your best application to see your training results',
        'user': request.user
    })

#def results(request):
#    return render_to_response(
#
#    'results.html',
#    {
#        'titlehead': 'Results for ' request.user,
#        'pagetitle': 'On ': request.results.match.date + ' at ' + request.results.match_h
#        'contentbody': 'Result:' + request.results.match_result + '. Handicap variation:' + request.results.handicap_variation
#    })
def player_results(request):
    return render_to_response(

    'results.html',
    {
        'titlehead': "Results",
        'pagetitle': "Players results",
        'matches': Match.objects.all(),

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
    'pagetitle' : "Player Information",
    'player': Player.objects.get(pk=player_id),

    })
