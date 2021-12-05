from rest_framework import serializers
from .models import STSRun, STSRunPlayer, Card, Relic, FloorResult, Battle, BattleCommand, VoteResult

class STSRunPlayerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = STSRunPlayer
		fields = ['screen_name', 'votes']


class CardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Card
		fields = ['card_id']


class RelicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Relic
		fields = ['relic_id']


class STSRunSerializer(serializers.ModelSerializer):
	players = STSRunPlayerSerializer(many=True)
	deck = CardSerializer(many=True)
	relics = RelicSerializer(many=True)

	class Meta:
		model = STSRun
		fields = ['id','victory', 'score', 'character_class', 'ascension', 'players', 'deck', 'relics', 'seed_string']

	def create(self, validated_data):
		player_data = validated_data.pop('players')
		deck_data = validated_data.pop('deck')
		relic_data = validated_data.pop('relics')
		run = STSRun.objects.create(**validated_data)

		for player in player_data: 	
			STSRunPlayer.objects.create(run=run, **player)

		for card in deck_data:
			Card.objects.create(run=run, **card)

		for relic in relic_data:
			Relic.objects.create(run=run, **relic)

		return run

	def update(self, instance, validated_data):
		instance.score = validated_data.get('score', instance.score)
		instance.seed_string = validated_data.get('seed_string', instance.seed_string)
		instance.ascension = validated_data.get('ascension', instance.ascension)
		instance.character_class = validated_data.get('character_class', instance.character_class)

		instance.save()

		return instance


class FloorResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = FloorResult
		fields = ['id', 'run', 'floor_num', 'hp_change']

	def create(self, validated_data):
		run = validated_data.pop('run')
		floor_result = FloorResult.objects.create(run=run, **validated_data)
		return floor_result


class BattleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Battle
		fields = ['run', 'start_state']

	def create(self, validated_data):
		run = validated_data.pop('run')
		battle = Battle.objects.create(run=run, **validated_data)
		return battle


class BattleCommandSerializer(serializers.ModelSerializer):
	class Meta:
		model = BattleCommand
		fields = ['floor_result', 'command_string', 'index']

	def create(self, validated_data):
		floor_result = validated_data.pop('floor_result')
		command = BattleCommand.objects.create(floor_result=floor_result, **validated_data)
		return command


class VoteResultSerializer(serializers.ModelSerializer):
	class Meta:
		model = VoteResult
		fields = ['run', 'floor_num', 'index', 'winning_vote']

	def create(self, validated_data):
		run = validated_data.pop('run')
		vote_result = VoteResult.objects.create(run=run, **validated_data)
		return vote_result