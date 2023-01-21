from django.db import models
import datetime

# Create your models here.

STATUS = (
    (0, "Active"),
    (1, "Inactive")
)

POSITIONS = (
    (0, "Top"),
    (1, "Jungle"),
    (2, "Mid"),
    (3, "ADC"),
    (4, "Support"),
)


class Region(models.Model):
    abbr = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=200, unique=True)
    place = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.abbr;


class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    established_since = models.DateField(auto_now=False, null=True)

    class Meta:
        ordering = ['-established_since']

    def __str__(self):
        return self.name


class Champion(models.Model):
    name = models.CharField(max_length=200, unique=True)
    health = models.IntegerField()
    mana = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=200, unique=True)
    current_team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)
    champ = models.ForeignKey(Champion, related_name='mains', on_delete=models.CASCADE)
    position = models.IntegerField(choices=POSITIONS, default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.current_team.__str__() + " " + self.name

    class Meta:
        ordering = ['name']


class Coach(models.Model):
    name = models.CharField(max_length=200, unique=True)
    current_team = models.OneToOneField(Team, related_name='coach', on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name


def year_choices():
    return ((r, r) for r in range(1984, datetime.date.today().year + 1))


def current_year():
    return datetime.date.today().year


class WorldChampion(models.Model):
    year = models.IntegerField('year', choices=year_choices(), default=current_year())
    champion = models.ForeignKey(Team, related_name='awards', on_delete=models.CASCADE)

    def __str__(self):
        return self.champion.__str__() + " - " + str(self.year)

    class Meta:
        ordering = ['-year']