from django.db import models


class Blog(models.Model):
    background = models.ImageField(upload_to='media/blog/')
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateField(blank=True)

    def __str__(self):
        return self.title