from .models import Books
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','author','descriptions','published_year']
        