from django.db import models


class Conference(models.Model):
	def __str__(self):
		return self.conference_text
	conference_text = models.CharField(max_length = 40)
	start_date = models.DateField('Conference Start Date')
	end_date = models.DateField('Conference End Date')
	publish_presentations_to_dropbox = models.BooleanField(default = False)
	
