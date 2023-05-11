from django.db import models

class Teacher(models. Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="media/teachers/")
    speciality = models.CharField(max_length=200)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagramm = models.URLField(blank=True)


    def __str__(self):
        return self.name






