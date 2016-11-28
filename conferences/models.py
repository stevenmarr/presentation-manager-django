from django.db import models


class Conference(models.Model):
	def __str__(self):
		return self.conference_text
	conference_text = models.CharField(max_length = 40)
	start_date = models.DateTimeField('Conference Start Date')
	end_date = models.DateTimeField('Conference End Date')
