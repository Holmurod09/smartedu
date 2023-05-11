from django.db import models


class Course(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.PositiveIntegerField(default=0, blank=True)
    length = models.CharField(max_length=50, blank=True)
    students = models.IntegerField(blank=True)

    def __str__(self):
        return self.title