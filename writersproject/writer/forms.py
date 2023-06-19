from django import forms
from .models import Writer

class WriterForm(forms.ModelForm):
    name = forms.CharField
    class Meta:
        model = Writer

        fields = ['name',
                  'year_of_birth',
                  'year_of_death',
                  'country_of_origin',
                  'number_of_novels',
                  'number_of_novellas',
                  'number_of_volumes_of_poetry',
                  ]