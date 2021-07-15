from rest_framework import serializers
from .models import STSRun, STSRunPlayer, Card, Relic

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
		fields = ['victory', 'score', 'character_class', 'ascension', 'players', 'deck', 'relics']

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