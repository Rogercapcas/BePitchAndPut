from django.forms import ModelForm
from models import Player, Match, Throw

class PlayerForm(ModelForm):
	class Meta:
		model = Player
		exclude = ('number_of_player','user')

class MatchForm(ModelForm):
    class Meta:
        model = Match
        exclude = ('match_number','user')

class ThrowForm(ModelForm):
	class Meta:
		model = Throw
		exclude = ('code','match','user')
