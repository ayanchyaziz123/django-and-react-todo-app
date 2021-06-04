from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

class ToDoProgrammingContest(models.Model):
    platform = models.CharField(max_length=120)
    staring_time = models.DateTimeField()
    ending_time = models.DateTimeField()
    description = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    