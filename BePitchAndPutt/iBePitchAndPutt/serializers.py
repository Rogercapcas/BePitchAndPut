from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Player, Field, Hole, Match, WeatherConditions, Throw


class PlayerSerializer(HyperlinkedModelSerializer):

	
	url = HyperlinkedIdentityField(view_name = 'iBePitchAndPutt: player-detail')
	matches = 
	class Meta:
		model = Player
		fields = ('url','name','number_of_player','birthday','stateOrProvince','city','street','zipCode','telephone','handicap')

class FieldSerializer(HyperlinkedModelSerializer):

	uri = HyperlinkedIdentityField(view_name = 'iBePitchAndPutt: field-detail')
	holes = 
	
	class Meta:
		model = Field
		fields = ('uri','FieldCode','field_name','stateOrProvince','city','street','zipCode','telephone','url','number_of_holes','par')


class HoleSerializer(HyperlinkedModelSerializer):




class MatchSerializer(HyperlinkedModelSerializer):

	
	url = HyperlinkedIdentityField(view_name = 'iBePitchAndPutt: match-detail')
	player = 
	weather = 

	class Meta:
		model = Match
		fields = ('url','match_number','player','date','weather')

class ThrowSerializer(HyperlinkedModelSerializer):

	
	url = HyperlinkedIdentityField(view_name = 'iBePitchAndPutt: throw-detail')
	class Meta:
		model = Throw
		fields = ('url','hole', 'match', 'score')
				

class WeatherConditionsSerializer(HyperlinkedModelSerializer):

	url = HyperlinkedIdentityField(view_name = 'iBePitchAndPutt: weatherConditions')
	matches = 
	class Meta:
		model = WeatherConditions
		fields = ('url','date','windSpeed','windDirection')