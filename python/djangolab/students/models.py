from django.db import models
from django.core.validators import MinValueValidator

from universities.models import UniversityModel

class StudentModel(models.Model):
	full_name = models.CharField(max_length=50)
	university = models.ForeignKey(UniversityModel, on_delete=models.PROTECT)
	admission_year = models.IntegerField()