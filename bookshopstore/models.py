from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=100, blank=False)
    publisher = models.CharField(max_length=100, blank=False)
    price = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to='bookcovers', default='cover.jpg')
    publishDate = models.CharField(max_length=100, blank=False)
    ISBN = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title


