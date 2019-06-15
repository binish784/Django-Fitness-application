from django import forms
from .models import log,logDetail
from django.forms.widgets import SelectDateWidget

from crispy_forms.layout import Layout,HTML,Submit,Field
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper

class LogForm(forms.ModelForm):

	start_time=forms.TimeField(widget=forms.TimeInput(format="%H:%M"))

	class Meta:
		model=log
		fields=['start_time','end_time']

	def __init__(self,*args,**kwargs):
		super(LogForm,self).__init__(*args,**kwargs)
		self.helper=FormHelper()
		self.helper.form_method="POST"
		self.fields['start_time'].label=False
		self.fields['end_time'].label=False
		self.helper.layout=Layout(
			Field('start_time',placeholder='Enter Start-Time '),
			Field('end_time',placeholder='Enter End-Time '),
			FormActions(
				HTML('<div>'),
				Submit('save','Record Log',css_class='btn btn-success'),
				HTML("<a href='{% url 'fitness:index' %}' class='btn btn-default'>Go Back</a>"),
				HTML('</div>'),
				),
			)

class LogDetailForm(forms.ModelForm):
	class Meta:
		model=logDetail
		fields=['exercise','num_of_sets','reps','weight_used']

