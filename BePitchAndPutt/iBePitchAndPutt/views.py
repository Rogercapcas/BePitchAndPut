from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.db.models import Sum
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from django.utils import timezone

#from rest_framework import generics, permissions
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from models import Player, Field, Hole, Match, Throw 
from serializers import PlayerSerializer, FieldSerializer, HoleSerializer, MatchSerializer, WeatherConditionsSerializer, ThrowSerializer

def mainpage(request):
    return render_to_response(

    'mainpage.html',
    {
        'titlehead': 'BePitchAndPutt app',
        'pagetitle': 'Welcome to BePitchAndPutt app',
        'contentbody': 'Your best application to see your training results',
        'user': request.user
    })

class PlayerList (ListView):
    model = Player
    queryset = Player.objects.all()
    context_object_name='Player_list'
    template_name='Player.html'

class FieldList (ListView):
    model = Field
    queryset = Field.objects.all()
    context_object_name='Field_list'
    template_name='Field.html'

class PlayerDetail(DetailView):
    model = Player
    template_name = 'Player_info.html' 

    def get_context_data(self, **kwargs):
        context = super(PlayerDetail, self).get_context_data(**kwargs)
        return context

"""
class PlayerCreate(CreateView):
    model = Player
    template_name = 'form.html'
    form_class = PlayerForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerCreate, self).form_valid(form)
"""


class MatchDetail(DetailView):
    model = Match
    template_name = 'Match_info.html'   
    def get_context_data(self, **kwargs):
        context = super(MatchDetail, self).get_context_data(**kwargs)
        return context

"""
class MatchCreate(CreateView):
    model = Match
    template_name = 'form.html'
    form_class = MatchForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MatchCreate, self).form_valid(form)
"""


class ThrowDetail(DetailView):
    model = Throw
    template_name = 'Throw_info.html'
    def get_context_data(self, **kwargs):
        context = super(ThrowDetail, self).get_context_data(**kwargs)
        return context

"""
class ThrowCreate(CreateView):
    model = Throw
    template_name = 'form.html'
    form_class = ThrowForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.match = Match.objects.get(id=self.kwargs['pk'])
        return super(ThrowCreate, self).form_valid(form)
"""

class FieldDetail(DetailView):
    model = Field
    template_name = 'Field_info.html'   
    def get_context_data(self, **kwargs):
        context = super(FieldDetail, self).get_context_data(**kwargs)
        return context

class HoleDetail(DetailView):
    model = Hole
    template_name = 'Hole_info.html'   
    def get_context_data(self, **kwargs):
        context = super(HoleDetail, self).get_context_data(**kwargs)
        return context

def rules (request):
    return render_to_response(

    'rules.html',
    {
        'titlehead': 'Rules',
        'pagetitle':'Rules of last version',
        
    })

"""
def actualWeather (request):
    return render_to_response(

    'weatherConditions.html',
    {
        'titlehead': 'Weather',
        'pagetitle': 'Weather conditions',
        'weather': weatherConditions.objects.get(pk=today),
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
"""