from django.db import models
from django.urls import reverse
from fitness.models import workout,WorkoutSet
from datetime import time

# Create your models here.

class log(models.Model):
	start_time=models.TimeField("Start Time")
	end_time=models.TimeField("End Time")
	created_on=models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.start_time) + " - " + str(self.end_time)

	def get_absolute_url(self):
		return reverse('log:logDetails',kwargs={'log_id':self.id})

class logDetail(models.Model):
	parent_log=models.ForeignKey(log,on_delete=models.CASCADE)
	exercise=models.ForeignKey(workout,on_delete=models.CASCADE)
	num_of_sets=models.IntegerField(blank=False,null=False)
	reps=models.IntegerField(blank=False,null=False)
	weight_used=models.DecimalField(decimal_places=1,max_digits=4)

	def __str__(self):
		return str(self.exercise)

	@property
	def get_set_id(self):
		return self.exercise.workout_set.id;