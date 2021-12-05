from django.db import models

# Create your models here.

# Contains the results of a single fun.
class STSRun(models.Model):
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	victory = models.BooleanField(default=False)
	score = models.IntegerField(default=0)
	character_class = models.CharField(max_length=64, default='')
	ascension = models.IntegerField(default=0)
	seed_string = models.CharField(max_length=64, default='')

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


class FloorResult(models.Model):
	id = models.AutoField(primary_key=True)
	run = models.ForeignKey(STSRun, related_name='floor_results', on_delete=models.CASCADE)
	floor_num = models.IntegerField(default=0)
	hp_change = models.IntegerField(default=0)


class Battle(models.Model):
	run = models.ForeignKey(STSRun, related_name='battles', on_delete=models.CASCADE)
	start_state = models.TextField()


class BattleCommand(models.Model):
	floor_result = models.ForeignKey(FloorResult, related_name='commands', on_delete=models.CASCADE)
	command_string = models.CharField(max_length=200, default='')
	index = models.IntegerField(default=0)


class VoteResult(models.Model):
	run = models.ForeignKey(STSRun, related_name='vote_results', on_delete=models.CASCADE)
	floor_num = models.IntegerField(default=0)
	index = models.IntegerField(default=0)
	winning_vote = models.TextField()