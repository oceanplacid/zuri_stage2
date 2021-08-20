from django import forms
from django.forms import ModelForm
#from .models import Venue


class Contact(ModelForm):
	class Meta:
		#Model = Venue
		fields = ("name", "phone", "email", "comment")