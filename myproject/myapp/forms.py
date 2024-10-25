
from django import forms
from .models import Books  # Ensure that the model name matches

class BookForms(forms.ModelForm):
    class Meta:
        model = Books  # Ensure that 'Books' is the correct model name
        fields = ['title', 'name', 'published']  # Ensure that field names are correct
