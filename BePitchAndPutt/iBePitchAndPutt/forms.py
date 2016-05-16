from django.forms import ModelForm
from models import Restaurant, Dish

class MatchForm(ModelForm):
    class Meta:
        model = Match
        exclude = ('player', 'date',)
