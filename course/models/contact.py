from django.db import models


class Contact(models. Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(blank=True)
    detail = models.TextField(blank=True)


    def __str__(self):
        return self.first_name

