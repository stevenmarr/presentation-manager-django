from django import forms

from .models import Presentation


class PresentationForm(forms.Form):
	class Meta:
		model = Presentation
		fields = ['presentation']
