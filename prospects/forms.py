from django import forms

from .models import Prospecters

class ProspectsForm(forms.ModelForm):

	class Meta:
		model = Prospecters
		exclude = ('sponsor','created_date','published_date')
		fields = '__all__'