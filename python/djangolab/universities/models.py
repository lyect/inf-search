from django.db import models

class UniversityModel(models.Model):
	full_name = models.CharField(max_length=255)
	abbreviation_name = models.CharField(max_length=255)
	founded_date = models.DateField()

	def __str__(self):
		return self.abbreviation_name
