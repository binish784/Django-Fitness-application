from django.contrib import admin
from .models import Fitness,WorkoutSet,workout,Profile

# Register your models here.

admin.site.register(Fitness)
admin.site.register(WorkoutSet)
admin.site.register(workout)
admin.site.register(Profile)