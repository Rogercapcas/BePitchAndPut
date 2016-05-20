from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Player, Field, Hole, Match, WeatherConditions, Throw


class PlayerSerializer(HyperlinkedModelSerializer):

	
	url = HyperlinkedIdentityField(view_name = 'player-detail')
	matches = HyperlinkedRelatedField(many=True, read_only=True, view_name='match-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Player
		fields = ('url','user','matches','name','number_of_player','birthdate','stateOrProvince','city','street','zipCode','telephone','handicap')

class FieldSerializer(HyperlinkedModelSerializer):

	uri = HyperlinkedIdentityField(view_name = 'field-detail')
	holes = HyperlinkedRelatedField(many=True, read_only=True, view_name='hole-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Field
		fields = ('uri','holes','user','FieldCode','field_name','stateOrProvince','city','street','zipCode','telephone','url','number_of_holes','par')


class MatchSerializer(HyperlinkedModelSerializer):

	url = HyperlinkedIdentityField(view_name = 'match-detail')
	player = HyperlinkedRelatedField(many=True, read_only=True, view_name='player-detail')
	user = CharField(read_only=True)	
	#weather = HyperlinkedRelatedField(many=True, read_only=True, view_name='iBePitchAndPutt:grade-detail')

	class Meta:
		model = Match
		fields = ('url','player','user','match_number','player','date','weather')

class ThrowSerializer(HyperlinkedModelSerializer):

    user = CharField(read_only=True)
    url = HyperlinkedIdentityField(view_name = 'throw-detail')


    class Meta:
		model = Throw
		fields = ('url','hole','user','match', 'score')
				
"""
class WeatherConditionsSerializer(HyperlinkedModelSerializer):

	url = HyperlinkedIdentityField(view_name = 'iBePitchAndPutt: weatherConditions')
	matches = HyperlinkedRelatedField(many=True, read_only=True, view_name='iBePitchAndPutt:match-detail')
	class Meta:
		model = WeatherConditions
		fields = ('url','date','windSpeed','windDirection')
	"""	