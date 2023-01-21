"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from eSportManager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('players/', views.players_view, name='players'),
    path('teams/', views.teams_view, name='teams'),
    path('coaches/', views.coachs_view, name='coachs'),
    path('regions/', views.regions_view, name='regions'),
    path('worlds/', views.worlds_view, name='worlds'),
    path('champions/', views.champions_view, name='champions'),
    path('teams/<int:pk>/', views.team_detail, name='team_detail'),
    path('regions/new', views.region_new, name='region_new'),
    path('champions/new', views.champion_new, name='champion_new'),
    path('coaches/new', views.coach_new, name='coach_new'),
    path('players/new', views.player_new, name='player_new'),
    path('teams/new', views.team_new, name='team_new'),
    path('worlds/new', views.world_new, name='world_new'),
]
