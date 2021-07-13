from rest_framework import serializers
from .models import STSRun

class STSRunSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = STSRun
		fields = ['victory', 'score']