from django.db import models


class ProgrammingLanguage(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)