from users.models import User
from conferences.models import Conference

from django.db import models

class Presentation(models.Model):
	def __str__(self):
		return self.session_title
	session_title = models.CharField(max_length = 100)
	date_and_time = models.DateTimeField('Presentation date and time')
	presentation = models.FileField(blank=True)
	presenter = models.ForeignKey(User, blank=True, null=True)
	conference = models.ForeignKey(Conference)
