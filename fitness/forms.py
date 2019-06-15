from django import forms
from django.contrib.auth.models import User

from .models import Fitness,WorkoutSet,workout,Profile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,HTML,Field,Submit
from crispy_forms.bootstrap import FormActions

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','email','first_name','last_name']

class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['birth_date','image','bio','base_weight','base_height']

class FitnessForm(forms.ModelForm):
	class Meta:
		model=Fitness
		fields=['weight']

	def __init__(self,*args,**kwargs):
		super(FitnessForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.fields['weight'].label=False	
		self.helper.form_method="POST"
		self.helper.layout=Layout(
			Field('weight',placeholder='Your Weight Today'),
			FormActions(
				Submit('save','Record',css_class='btn btn-primary'),
				)
			)

class WorkoutSetForm(forms.ModelForm):
	class Meta:
		model=WorkoutSet
		fields=['name']

	def __init__(self,*args,**kwargs):
		super(WorkoutSetForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.fields['name'].label=False
		self.fields.form_method="POST"
		self.helper.layout=Layout(
			Field('name',placeholder='Enter Name of Workout-set'),
			FormActions(
				HTML("<div>"),
				Submit('save','Create Set',css_class='btn btn-success'),
				HTML("</div>"),
				),
			)


class WorkoutForm(forms.ModelForm):
	class Meta:
		model=workout
		fields=['name','description']

	def __init__(self,*args,**kwargs):
		super(WorkoutForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.fields['name'].label=False
		self.fields['description'].label=False
		self.fields.form_method="POST"
		self.helper.layout=Layout(
			Field('name',placeholder='Enter Name of Workout'),
			Field('description',placeholder='Enter workout description',rows=3),
			FormActions(
				Submit('save','Add Workout',css_class='btn btn-primary'),
				),
			)

