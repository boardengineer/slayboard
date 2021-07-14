from django.db import models

# Create your models here.
class STSRun(models.Model):
	victory = models.BooleanField(default=False)
	score = models.IntegerField(default=0)

class STSRunPlayer(models.Model):
	run = models.ForeignKey(STSRun, related_name='players', on_delete=models.CASCADE)
	screen_name = models.CharField(max_length=64)
	votes = models.IntegerField(default=0)