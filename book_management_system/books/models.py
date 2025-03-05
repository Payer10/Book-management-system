from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    descriptions = models.TextField()
    published_year = models.PositiveBigIntegerField()

    def __str__(self):
        return self.title
