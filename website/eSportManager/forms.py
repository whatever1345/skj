from django import forms
from .models import Player, Team, Coach, WorldChampion, Region, Champion


class RegionForm(forms.ModelForm):

    class Meta:
        model = Region
        fields = ('abbr', 'name', 'place',)


class ChampionForm(forms.ModelForm):

    class Meta:
        model = Champion
        fields = ('name', 'health', 'mana',)


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('name', 'region', 'status', 'established_since',)


class CoachForm(forms.ModelForm):

    class Meta:
        model = Coach
        fields = ('name', 'current_team', 'status',)


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'current_team', 'champ', 'position', 'status',)


class WorldForm(forms.ModelForm):

    class Meta:
        model = WorldChampion
        fields = ('champion', 'year',)
