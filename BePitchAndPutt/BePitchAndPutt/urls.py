"""BePitchAndPutt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.auth.models import User

from iBePitchAndPutt.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^player/$',PlayerList.as_view(),name='Player_list'),
    url(r'^player/(?P<pk>\d+)/$',PlayerDetail.as_view(),name='Player_detail'),
    url(r'^rules/',rules),
    url(r'^match/(?P<pk>\d+)/$',MatchDetail.as_view(),name="Match_detail"),
    url(r'throw/(?P<pk>\d+)/$', ThrowDetail.as_view(), name="Throw_detail"),
    url(r'^field/$',FieldList.as_view(),name="Field_list"),
    url(r'^field/(?P<pk>\d+)/$',FieldDetail.as_view(),name="Field_detail"),

]

'''  

    



    url(r'^holes/(?P<pk>\d+)/$',HoleDetail.as_view,name="Hole_detail"),


    url(r'^field/$',FieldList.as_view(),name="Field_list"),
    url(r'^field/(?P<pk>\d+)/$',FieldDetail.as_view(),name="Field_detail"),

    url(r'^match/(?P<pk>\d+)/$',MatchDetail.as_view(),name="Match_detail"),


    
    url(r'^actualWeather/$',actualWeather),
    url(r'^results/(?P<pk>\d+)/$',player_results),
    url(r'^$', mainpage, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),

    
    #RESTful API
    url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/player/$',
        APIPlayerList.as_view(), name='player-list')
    url(r'^api/player/(?P<pk>\d+)/$',
        APIPlayerDetail.as_view(), name='player-detail',)
    url(r'^api/hole/$',
        APIHoleList.as_view(), name='hole-list')
    url(r'^api/hole/(?P<pk>\d+)/$',
        APIHoleDetail.as_view(), name='hole-detail',)
    url(r'^api/field/$',
        APIPlayerList.as_view(), name='field-list')
    url(r'^api/field/(?P<pk>\d+)/$',
        APIFieldDetail.as_view(), name='field-detail',)'''