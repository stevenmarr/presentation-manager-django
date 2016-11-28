from users.models import User
from conferences.models import Conference

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

class Presentation(models.Model):
	def __str__(self):
		return self.session_title

	def clean(self):
	# Do not allow session dates outside of conference dates
		if self.date_and_time.date() < self.conference.start_date or self.date_and_time.date() > self.conference.end_date:
			raise ValidationError(_('Presentation date must be during assigned conference.'))
        
	session_title = models.CharField(max_length = 100)
	date_and_time = models.DateTimeField('Presentation date and time')
	presentation = models.FileField(blank=True)
	presenter = models.ForeignKey(User, blank=True, null=True)
	conference = models.ForeignKey(Conference)

	def get_absolute_url(self):
		return "/presentations/list"
