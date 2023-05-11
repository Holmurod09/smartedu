from django.db import models


class Pricing(models. Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    number_courses = models.IntegerField(blank=True)
    email_akk = models.CharField(max_length=200)
    arrival_days = models.IntegerField(blank=True)
    empty_course = models.IntegerField(blank=True)
    busy_courses = models.IntegerField(blank=True)

    def __str__(self):
        return self.title


