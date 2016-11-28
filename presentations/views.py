from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Presentation


@login_required
def index(request, conference_id):
	presentations = Presentation.objects.filter(conference_id=conference_id)
	context = {'presentations': presentations, 'conference_id': conference_id}
	return render(request, 'presentations/index.html', context)
