from django.db import models
import datetime

# Course for the term, can input "other" if not school related

class Course(models.Model):
    name            = models.CharField(max_length = 100)
    subject         = models.CharField(max_length = 100)
    term            = models.CharField(max_length = 100)
    description     = models.TextField()

    def __str__(self):
        return self.name

# Entry for what user has TO DO

class Entry(models.Model):
    title           = models.CharField(max_length = 100)
    course          = models.ForeignKey(Course)
    due_date        = models.DateField(default = datetime.date.today)
    description     = models.TextField()

    def __str__(self):
        return self.title