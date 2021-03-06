from django.shortcuts import render, render_to_response

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView

from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView, UpdateView


from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from models import Player, Field, Hole, Match, Throw 
from serializers import PlayerSerializer, FieldSerializer, MatchSerializer, ThrowSerializer
from forms import *




class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'form.html'

def mainpage(request):
    return render_to_response(

    'Mainpage.html',
    {
        'titlehead': 'BePitchAndPutt app',
        'pagetitle': 'Benvingut a BePitchAndPutt app',
        'contentbody': 'La millor aplicacio per guardar els resultats dels teus entrenaments',
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


class PlayerCreate(LoginRequiredMixin, CreateView):
    model = Player
    template_name = 'form.html'
    form_class = PlayerForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PlayerCreate, self).form_valid(form)

class MatchDetail(DetailView):
    model = Match
    template_name = 'Match_info.html'   
    def get_context_data(self, **kwargs):
        context = super(MatchDetail, self).get_context_data(**kwargs)
        return context


class MatchCreate(LoginRequiredMixin,CreateView):
    model = Match
    template_name = 'form.html'
    form_class = MatchForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.player = get_object_or_404(Player, pk=self.kwargs['pk'])
        return super(MatchCreate, self).form_valid(form)


class ThrowDetail(DetailView):
    model = Throw
    template_name = 'Throw_info.html'
    def get_context_data(self, **kwargs):
        context = super(ThrowDetail, self).get_context_data(**kwargs)
        return context

class ThrowCreate(LoginRequiredMixin,CreateView):
    model = Throw
    template_name = 'form.html'
    form_class = ThrowForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.match = get_object_or_404(Match, pk=self.kwargs['pk'])
        return super(ThrowCreate, self).form_valid(form)

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

    'Rules.html',
    {
        'titlehead': 'Rules',
        'pagetitle':'Ultima versio de les normes',
        
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


class APIMatchDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Match
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class APIThrowDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Throw
    queryset = Throw.objects.all()
    serializer_class = ThrowSerializer
