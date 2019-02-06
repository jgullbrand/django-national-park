from django.db import models

class TravelEntry(models.Model):
	park_name = models.CharField(max_length = 25)
	author_name = models.CharField(max_length = 25)
	text = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return ("Entry # {}".format(self.id))	

	class Meta:
		verbose_name_plural = "TravelEntries"	
