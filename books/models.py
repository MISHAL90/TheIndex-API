from django.db import models
from django.urls import reverse


class Author(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    imageUrl = models.CharField(max_length=255, blank=True, default="")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('author-detail', args=[self.id])

    class Meta:
        ordering = ['last_name', 'first_name']


class Book(models.Model):
    COLOR_CHOICES = (
        ('red', 'red'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('yellow', 'yellow'),
        ('black', 'black'),
        ('white', 'white'),
        ('grey', 'grey'),
        ('purple', 'purple'),
        ('orange', 'orange'),
    )
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    color = models.CharField(max_length=255, choices=COLOR_CHOICES)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])

    class Meta:
        ordering = ['title', ]
