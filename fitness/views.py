from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import datetime


from django.contrib.auth.decorators import login_required

from .models import Fitness,WorkoutSet,workout
from .forms import FitnessForm,WorkoutSetForm,WorkoutForm,ProfileForm,UserForm

# Create your views here.

@login_required
def IndexView(request):
	form=FitnessForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse_lazy('fitness:index'))
	recent_Fitness_upload=Fitness.objects.order_by('-pk')[:1]
	if recent_Fitness_upload.exists():
		for upload in recent_Fitness_upload:
			if upload.date==datetime.date.today():
				context={
					'recent_weight':recent_Fitness_upload,
				}
			else:
				context={
					'form':form,
					'recent_weight':recent_Fitness_upload,
				}
			return render(request,'fitness/index.html',context)
	return render(request,'fitness/index.html',{'form':form})


@login_required
def StatsView(request):
	return render(request,'fitness/weight-statistics.html',{})

@login_required
def SetWorkoutView(request):
	form=WorkoutSetForm(request.POST or None)
	available_sets=WorkoutSet.objects.all()
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(form.instance.get_absolute_url())
	return render(request,'fitness/set-workout.html',{'form':form,'sets':available_sets})

def SetDetailView(request,set_id):
	selected_set=get_object_or_404(WorkoutSet,pk=set_id)
	form=WorkoutForm(request.POST or None)
	if form.is_valid():
		form.instance.workout_set=selected_set
		form.save()
		return HttpResponseRedirect(selected_set.get_absolute_url())
	return render(request,'fitness/set-details.html',{'selected_set':selected_set,'form':form})

@login_required
def ProfileView(request):
	return render(request,'fitness/profile.html',{})

@login_required
def UpdateProfileView(request):
	if request.POST:
		profileForm=ProfileForm(request.POST or None,request.FILES,instance=request.user.profile)
		userForm=UserForm(request.POST or None,instance=request.user)
		if profileForm.is_valid() and userForm.is_valid():
			user_instance=userForm.save(commit=False)
			profile_instance=profileForm.save(commit=False)
			profile_instance.user=request.user;
			user_instance.save()
			profile_instance.save()
			return HttpResponseRedirect(reverse_lazy('fitness:profile'));
	else:
		profileForm=ProfileForm(None,instance=request.user.profile)
		userForm=UserForm(None,instance=request.user)	
	context={
		'user_form':userForm,
		'profile_form':profileForm,
	}
	return render(request,'fitness/updateProfile.html',context)

@login_required
def DetailWorkoutView(request,workout_id):
	selected_workout=get_object_or_404(workout,pk=workout_id)
	context={
		'workout':selected_workout,
	}
	return render(request,'fitness/workoutDetail.html',context)
