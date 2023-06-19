from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField
    class Meta:
        model = Book

        fields = ['title',
                  'writer',
                  ]