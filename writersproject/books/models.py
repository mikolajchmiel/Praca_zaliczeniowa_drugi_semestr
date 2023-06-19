from django.db import models
class Book(models.Model):
    title = models.CharField(blank=False, max_length=150, default='Unknown')
    writer = models.ForeignKey('writer.Writer', on_delete=models.DO_NOTHING, related_name='books')

    def __str__(self):
        return f'{self.id}: {self.title}'

