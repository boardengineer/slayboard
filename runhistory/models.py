from django.db import models

# Create your models here.

# Contains the results of a single fun.
class STSRun(models.Model):
	victory = models.BooleanField(default=False)
	score = models.IntegerField(default=0)
	character_class = models.CharField(max_length=64, default='')
	ascension = models.IntegerField(default=0)

# Stats about a player (voter) for a single run
class STSRunPlayer(models.Model):
	run = models.ForeignKey(STSRun, related_name='players', on_delete=models.CASCADE)
	screen_name = models.CharField(max_length=64)
	votes = models.IntegerField(default=0)


class Card(models.Model):
	run = models.ForeignKey(STSRun, related_name='deck', on_delete=models.CASCADE)
	card_id = models.CharField(max_length=64, default='')


class Relic(models.Model):
	run = models.ForeignKey(STSRun, related_name='relics', on_delete=models.CASCADE)
	relic_id = models.CharField(max_length=64, default='')