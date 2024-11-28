from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn=models.CharField(max_length=15)

    def __str__(self):
        return f"{self.title} {self.id}"