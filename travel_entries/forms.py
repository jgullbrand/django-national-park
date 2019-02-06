from django import forms

from .models import TravelEntry

class EntryForm(forms.ModelForm):
	class Meta:
		model = TravelEntry
		fields = ["park_name", "author_name", "text"]
		widgets = {
			"park_name": forms.TextInput(attrs={"placeholder": "National Park", 'size': 35,}),
			"author_name": forms.TextInput(attrs={"placeholder": "Your Name", 'size': 35}),
			"text": forms.Textarea(attrs={"placeholder": "Tell us about your experience at the park:" , 'cols': 71, 'rows': 10})
		}