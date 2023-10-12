from django.db import models

# Create your models here.

class Tech(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    year = models.IntegerField()
    img = models.ImageField(upload_to='project_images/')
    repository = models.URLField()
    technologies = models.ManyToManyField(Tech)

    def __str__(self):
        return f"{self.name} - ({self.year})"