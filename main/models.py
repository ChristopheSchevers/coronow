from django.db import models

class Region(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    source_file = models.FileField(upload_to='uploads/',blank=True)

    def __str__(self):
        return self.title

class Measure(models.Model):
    title = models.CharField(max_length=200)
    modtime = models.DateField(auto_now=True)
    content = models.TextField(blank=True)
    region = models.ManyToManyField(Region)

    def __str__(self):
        return self.title