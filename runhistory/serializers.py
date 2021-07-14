from rest_framework import serializers
from .models import STSRun, STSRunPlayer

class STSRunPlayerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = STSRunPlayer
		fields = ['screen_name', 'votes']


class STSRunSerializer(serializers.ModelSerializer):
	players = STSRunPlayerSerializer(many=True)

	class Meta:
		model = STSRun
		fields = ['victory', 'score', 'players']

	def create(self, validated_data):
		player_data = validated_data.pop('players')
		run = STSRun.objects.create(**validated_data)
		for player in player_data:
			STSRunPlayer.objects.create(run=run, **player)
		return run