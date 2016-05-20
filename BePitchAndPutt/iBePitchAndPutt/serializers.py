from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Player, Field, Hole, Match, WeatherConditions, Throw


class PlayerSerializer(HyperlinkedModelSerializer):

	user = CharField(read_only=True)
	class Meta:
		model = Player
		fields = ('user','name','number_of_player','birthday','stateOrProvince','city','street','zipCode','telephone','handicap')

class FieldSerializer(HyperlinkedModelSerializer):

	user = CharField(read_only=True)
	class Meta:
		model = Field
		fields = ('user','FieldCode','field_name','stateOrProvince','city','street','zipCode','telephone','url','number_of_holes','par')

class HoleSerializer(HyperlinkedModelSerializer):

	user = CharField(read_only=True)
	class Meta:
		model = Hole
		fields = ('user','field','hole_number','meters','handicap_hole')

class MatchSerializer(HyperlinkedModelSerializer):

	user = CharField(read_only=True)
	class Meta:
		model = Match
		fields = ('user','match_number','player','date','weather')

class ThrowSerializer(HyperlinkedModelSerializer):

	user = CharField(read_only=True)
	class Meta:
		model = Throw
		fields = ('hole', 'match', 'score')
		
		

class WeatherConditionsSerializer(HyperlinkedModelSerializer):

	user = CharField(read_only=True)
	class Meta:
		model = WeatherConditions
		fields = ('user','date','windSpeed','windDirection')