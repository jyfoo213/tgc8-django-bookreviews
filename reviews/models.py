from django.db import models
from books.models import Book

# Create your models here.


class Review(models.Model):
    title = models.CharField(blank=False, max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    # if no date is provided, use the current date on the server
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
