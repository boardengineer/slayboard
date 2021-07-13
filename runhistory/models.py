from django.db import models

# Create your models here.
class STSRun(models.Model):
	victory = models.BooleanField(default=False)
	score = models.IntegerField(default=0)