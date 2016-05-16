from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.db.models import Sum


from django.contrib.auth.models import User
from django.utils import timezone

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from models import Player, Field, Hole, Match,Rule
from serializers import PlayerSerializer, FieldSerializer, HoleSerializer, MatchSerializer, RuleSerializer, WeatherConditionsSerializer

def mainpage(request):
    return render_to_response(

    'mainpage.html',
    {
        'titlehead': 'BePitchAndPutt app',
        'pagetitle': 'Welcome to BePitchAndPutt app',
        'contentbody': 'Your best application to see your training results',
        'user': request.user
    })
def pdf (request):
    return render_to_response(
    'pdf.html',
    )

def player_results(request, player_id, match_number):
    return render_to_response(

    'results.html',
    {

        'titlehead': "Results",
        'pagetitle': Player.objects.get(pk=player_id),
        'matches': Match.objects.filter(player=player_id,match_number= match_number).all(),
        'match_result' : Match.objects.filter(player=player_id,match_number= match_number).aggregate(Sum('hole_result')),

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
        'pagetitle': 'Field information',
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
        'weather': WeatherConditions.objects.get(pk=today),
    })


#RESTful API


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class APIPlayerList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Player
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class APIPlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Player
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class APIFieldList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Field
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

class APIFieldDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Field
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

class APIHoleList(generics.ListCreateAPIView)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Hole
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer

class APIHoleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Hole
    queryset = Hole.objects.all()
    serializer_class = HoleSerializer



class APIMatchList(generics.ListCreateAPIView)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Match
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class APIMatchDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Match
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

