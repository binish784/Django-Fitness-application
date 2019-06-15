from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from fitness.models import Fitness,workout,WorkoutSet
from .serializer import WeightSerializer,WorkoutSerializer,WorkoutSetSerializer

from django.utils import timezone
from django.http import Http404
from datetime import timedelta,date
from dateutil.relativedelta import relativedelta


class WeightWeekStat(generics.ListAPIView):

	authentication_classes = (SessionAuthentication,BasicAuthentication)
	permission_classes = (IsAuthenticated,)

	model=Fitness
	serializer_class=WeightSerializer
	#queryset=Fitness.objects.all()

	def get(self,request,format=None):
		#end_date=date.today()
		#start_date=end_date - timedelta(days=6)
		#Weights= Fitness.objects.filter(date__range=[start_date, end_date])
		Weights=Fitness.objects.order_by('pk')[:7]
		recent_weight=[]
		label=[]
		max_weight=0
		for each in Weights:
			recent_weight.append(each.weight)
			month_date=str(each.date)[5:]
			label.append(month_date)
		if len(recent_weight) < 7:
			while len(recent_weight) < 7 :
				recent_weight.insert(0,request.user.profile.base_weight)
				label.insert(0,"Base")
		max_weight=max(recent_weight)
		context={
			'labels':label,
			'weights':recent_weight,
			'max_weight':max_weight,
		}
		return Response(context)


class WeightMonthStat(generics.ListAPIView):

	authentication_classes=(BasicAuthentication,SessionAuthentication)
	permission_classes=(IsAuthenticated,)

	model=Fitness
	serializer_class=WeightSerializer

	def get(self,request,format=None):
		weights=[]
		labels=[]
		month=1
		today=date.today()
		current_year=today.year
		first_jan=date(current_year,1,1)
		for month in range(1,today.month+1):
			month_start=date(current_year,month,1)
			month_end=first_jan+relativedelta(months=+month)-relativedelta(days=+1)
			month_weights=Fitness.objects.filter(date__range=[month_start,month_end])
			tot=0
			for entries in month_weights:
				tot=entries.weight+tot
			entries_in_month=month_weights.count()
			if entries_in_month == 0:
				entries_in_month=1
			month_avg_weight=float(tot/entries_in_month)
			month_label = month_start.strftime('%B')
			weights.append(month_avg_weight)
			labels.append(month_label)
		context={
			'labels':labels,
			'weights':weights,
		}
		return Response(context)

class WorkoutListAPIView(generics.ListAPIView):

	authentication_classes=(BasicAuthentication,SessionAuthentication)
	permission_classes=(IsAuthenticated,)

	serializer_class=WorkoutSerializer
	model=workout
	
	def get_queryset(self,*args,**kwargs):
		#try:
			pk=self.kwargs['pk']
			print("primary key " + str(pk))
			selected_set=WorkoutSet.objects.get(pk=pk)
			exercises=workout.objects.filter(workout_set=selected_set)
			return (exercises)
		#except: 
		#	raise Http404
	
	#def get_object(self,pk):
	#	try:
	#		selected_set=WorkoutSet.objects.get(pk=pk)
	#		exercises=workout.objects.filter(workout_set=selected_set)
	#		return (exercises)
	#	except: 
	#		raise Http404
		

	#def get(self,request,pk,format=None):
	#	exe_object=self.get_object(pk)
	#	serializer=WorkoutSerializer(exe_object,many=True)
	#	return Response(serializer.data)


class WorkoutSetAPIView(generics.ListAPIView):

	authentication_classes=(SessionAuthentication,BasicAuthentication)
	permission_classes=(IsAuthenticated,)

	serializer_class=WorkoutSetSerializer
	model=WorkoutSet

	def get_queryset(self):
		return WorkoutSet.objects.all()













