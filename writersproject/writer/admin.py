from django.contrib import admin
from .models import Writer

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    fields = ('name', 'year_of_birth', 'year_of_death', 'country_of_origin','number_of_novels','number_of_novellas','number_of_volumes_of_poetry','number_of_books')
    list_display = ('name', 'year_of_birth', 'year_of_death','country_of_origin', 'number_of_books')
    readonly_fields = ['number_of_books']

    def number_of_books(self, obj):
        return obj.number_of_novels + obj.number_of_novellas + obj.number_of_volumes_of_poetry
