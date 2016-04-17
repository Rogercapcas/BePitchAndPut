#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Get weather from weather underground
Created on 11/22/2014
Using XML as format, minidom
@author: carlesm
'''

import sys
import requests
import json

api_key = dc9eb5860cc66ad2


class WeatherClient(object):


    """Will access wunderground to gather weather information
    Provides access to wunderground API
    (http://www.wunderground.com/weather/api)
    Provides methods:
        conditions
    """

    url_base = 'http://api.wunderground.com/api/'
    url_services = {
        "conditions": "/conditions/q/CA/"
    }

    def __init__(self, apikey):
        super(WeatherClient, self).__init__()
        self.api_key = apikey


    def conditions(self, location):
        """
        Accesses wunderground conditions information for the given location
        """
        resp_format = "json"
        url = WeatherClient.url_base + api_key + \
            WeatherClient.url_services[
                "conditions"] + location + "." + resp_format
        r = requests.get(url)

        jsondata = json.loads(r.text)
        return jsondata["conditions"]

def get_wind_direction(conditions):
    return conditions["wind_dir"]

def get_wind_speed (conditions):
    return coditions["wind_kph"]

if __name__ == "__main__":
    weatherclient = WeatherClient(api_key)
    win_direction = get_wind_direction(weatherclient.conditions("Guissona"))
    wind_speed = get_wind_speed(weatherclient.conditions("Guissona"))
