from django.db import models
from django.utils import timezone

now = timezone.now()
class Category(models.Model):
    name = models.CharField(max_length=200)

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)

class Movie(models.Model):
    name = models.CharField(max_length=300)
    release_date = models.DateTimeField(blank=True, null=True)
    imdb_link = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category)

    def remaining_time(self):
        remaining_time = timezone.now().date()-self.release_date.date()
        return str(remaining_time)

    def name_plus(self):
        nam = self.name +"love"
        return nam

class News(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    site = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category)

class Calendar(models.Model):
    title = models.CharField(max_length=300)
    date_when = models.DateTimeField(blank=True, null=True)
