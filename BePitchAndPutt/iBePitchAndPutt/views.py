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


def player_results(request, name, match_number):
    return render_to_response(

    'results.html',
    {
        'titlehead': "Results",
        'pagetitle': "Players results",
        'player_name': Player.objects.get(name=name),
        'matches':Match.objects.filter(player=Player.objects.get(name=name),match_number= match_number).all(),

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

    'player_info.html',
    {
        'titlehead' : "Player info",
        'pagetitle' : "Player Information",
        'player': Player.objects.get(pk=player_id),
    })

def holes(request):
    model = Hole
    return render_to_response(

    'Hole.html',
    {
        'titlehead' : "Holes",
        'pagetitle' : "Holes",
        'holes': Hole.objects.all(),
    })

def hole_info (request, hole_number):
    return render_to_response(

    'holes_info.html',
    {
        'titlehead' : "Hole info",
        'pagetitle' : "Hole information",
        'hole' : Hole.objects.get(pk=hole_number),
    })

def field (request):
    model = Field
    return render_to_response(

    'Field.html',
    {
    'titlehead': "Fields",
    'pagetitle': "Fields",
    'fields': Field.objects.all(),
    })

def field_info(request, FieldCode):
    return render_to_response(
    'Field_info.html',
    {
        'titlehead':'Field info',
        'pagetitle': 'Field imformation',
        'field': Field.objects.get(pk=FieldCode),

    })

def rules (request):
    return render_to_response(

    'rules.html',
    {
        'titlehead': 'Rules',
        'pagetitle':'Rules of last version',
        'rules': Rule.objects.all(),
    })
def actualWeather (request):
    return render_to_response(

    'weatherConditions.html',
    {
        'titlehead': 'Weather',
        'pagetitle': 'Weather conditions',
        'weather': WeatherConditions.objects.all(),
    })
