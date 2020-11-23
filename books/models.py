from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

# we want to have a Book table inside our database


class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Book(models.Model):
    # what are the fields (aka attributes) of this table

    # eqv. title VARCHAR(255) NOT NULL
    title = models.CharField(blank=False, max_length=255)

    # eqv. ISBN VARCHAR(255) NOT NULL
    ISBN = models.CharField(blank=False, max_length=255)

    # eqv. desc TEXT NOT NULL
    desc = models.TextField(blank=False)

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    tags = models.ManyToManyField('Tag')

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    authors = models.ManyToManyField('Author')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    cover = CloudinaryField()

    # toString function -- it allows us to state the string representation
    # of a class
    def __str__(self):
        return self.title


class Publisher(models.Model):
    # the fields (aka attributes) of the table
    name = models.CharField(blank=False, max_length=100)
    email = models.CharField(blank=False, max_length=100)
    website = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    dob = models.DateField(blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(blank=False, max_length=100)

    def __str__(self):
        return self.title