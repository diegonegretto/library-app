from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=200)
    biography = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="authors/", blank=True, null=True)

    def __str__(self):
        return self.name
