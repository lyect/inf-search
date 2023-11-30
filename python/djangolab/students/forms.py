from django import forms
from django.core.validators import MinValueValidator

import datetime

from universities.models import UniversityModel

class StudentsCreateForm(forms.Form):
	full_name = forms.CharField(label="Name", max_length=255)
	university = forms.ModelChoiceField(label="University", queryset=UniversityModel.objects.all())
	admission_year = forms.IntegerField(label="Admission year")

	university.empty_label = "--- Select ---"
		