from django.db import models
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	birth_date=models.DateField(blank=True,null=True)
	image=models.ImageField(null=True,blank=True)
	bio=models.TextField(max_length=500,blank=True,null=True)
	base_height=models.DecimalField(max_digits=5,decimal_places=4,blank=True,null=True)
	base_weight=models.DecimalField(max_digits=6,decimal_places=4,default=70)


	def __str__(self):
		return self.user.username

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
	instance.profile.save()

class Fitness(models.Model):
	weight=models.DecimalField(max_digits=5,decimal_places=2)
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return str(self.weight)

class WorkoutSet(models.Model):
	name=models.CharField(max_length=200)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('fitness:set-detail',kwargs={'set_id':self.id})

class workout(models.Model):
	name=models.CharField(max_length=200)
	description=models.TextField(max_length=1500)
	workout_set=models.ForeignKey(WorkoutSet,on_delete=models.CASCADE)

	def __str__(self):
		return self.name
