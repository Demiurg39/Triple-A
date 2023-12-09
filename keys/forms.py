from django import forms
from keys.models import Keys
class RentKeyForm(forms.ModelForm):
    class Meta:
        model = Keys
        fields = ['period']

