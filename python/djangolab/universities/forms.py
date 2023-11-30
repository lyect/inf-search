from django import forms

from djangolab import settings

class UniversitiesCreateForm(forms.Form):
	full_name = forms.CharField(label="Full name", max_length=255)
	abbreviation_name = forms.CharField(label="Abbreviation", max_length=255)
	founded_date = forms.DateField()
		