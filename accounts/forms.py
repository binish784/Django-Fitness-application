from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	class meta:
		model=User
		fields=['username','password']
		