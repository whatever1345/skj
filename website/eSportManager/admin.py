from django.contrib import admin
from .models import Team, Player, Champion, Coach, Region, WorldChampion
# Register your models here.
models = [Team, Player, Champion, Coach, Region, WorldChampion]
for model in models:
    admin.site.register(model)
