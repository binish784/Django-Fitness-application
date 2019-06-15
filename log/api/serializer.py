from rest_framework import serializers
from log.models import logDetail,log
from fitness.models import workout,WorkoutSet
from fitness.api.serializer import WorkoutSerializer

class LogDetailReadSerializer(serializers.ModelSerializer):
	exercise=serializers.SlugRelatedField(read_only=True,slug_field='name')
	class Meta:
		model=logDetail
		fields=('id','parent_log','exercise','num_of_sets','reps','weight_used')

class LogDetailWriteSerializer(serializers.ModelSerializer):
	class Meta:
		model=logDetail
		fields=('parent_log','exercise','num_of_sets','reps','weight_used')
