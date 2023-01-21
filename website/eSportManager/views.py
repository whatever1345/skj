from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Player, Team, Coach, WorldChampion, Region, Champion
from .forms import RegionForm, ChampionForm, CoachForm, TeamForm, PlayerForm, WorldForm


def home(request):
    li = ["Teams", "Players", "Coaches", "World Champions", "Regions", "In-game Champions"]
    urls = ["/teams", "/players", "/coaches", "/worlds", "/regions", "/champions"]
    zip_list = zip(li, urls)
    return render(request, 'home.html', {'list': zip_list})


def players_view(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})


def teams_view(request):
    teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': teams})


def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    players = team.players.all()
    coach = team.coach

    print(coach)
    return render(request, 'team.html', {'team': team, 'players': players, "coach": coach})


def coachs_view(request):
    coachs = Coach.objects.all()
    return render(request, 'coachs.html', {'coachs': coachs})


def worlds_view(request):
    worlds = WorldChampion.objects.all()
    return render(request, 'worlds.html', {'worlds': worlds})


def regions_view(request):
    regions = Region.objects.all()
    return render(request, 'regions.html', {'regions': regions})


def champions_view(request):
    champions = Champion.objects.all()
    return render(request, 'champions.html', {'champions': champions})


def region_new(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            region = form.save(commit=False)
            region.save()
            return redirect('regions')
    else:
        form = RegionForm()
    return render(request, 'forms/region_new.html', {'form': form})


def champion_new(request):
    if request.method == 'POST':
        form = ChampionForm(request.POST)
        if form.is_valid():
            champ = form.save(commit=False)
            champ.save()
            return redirect('champions')
    else:
        form = ChampionForm()
    return render(request, 'forms/champion_new.html', {'form': form})


def coach_new(request):
    if request.method == 'POST':
        form = CoachForm(request.POST)
        if form.is_valid():
            coach = form.save(commit=False)
            coach.save()
            return redirect('coachs')
    else:
        form = CoachForm()
    return render(request, 'forms/coach_new.html', {'form': form})


def team_new(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            return redirect('teams')
    else:
        form = TeamForm()
    return render(request, 'forms/team_new.html', {'form': form})


def player_new(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.save()
            return redirect('players')
    else:
        form = PlayerForm()
    return render(request, 'forms/player_new.html', {'form': form})


def world_new(request):
    if request.method == 'POST':
        form = WorldForm(request.POST)
        if form.is_valid():
            world = form.save(commit=False)
            world.save()
            return redirect('worlds')
    else:
        form = WorldForm()
    return render(request, 'forms/world_new.html', {'form': form})