from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from .forms import PresentationForm
from .models import Presentation


class PresentationListView(generic.ListView):
	def get_queryset(self):
		current_user = self.request.user
		return Presentation.objects.filter(presenter_id=current_user.id)

	
class UpdateView(generic.UpdateView):
	model = Presentation
	fields = ['session_title','presentation']
	template_name = 'presentations/update.html'

