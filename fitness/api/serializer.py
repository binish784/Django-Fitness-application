from rest_framework import serializers
from fitness.models import Fitness,workout,WorkoutSet

class WeightSerializer(serializers.ModelSerializer):
	class Meta:
		model=Fitness
		fields=['weight']

class WorkoutSerializer(serializers.ModelSerializer):
	class Meta:
		model=workout
		fields=('id','name')

class WorkoutSetSerializer(serializers.ModelSerializer):
	class Meta:
		model=WorkoutSet
		fields=['id','name']