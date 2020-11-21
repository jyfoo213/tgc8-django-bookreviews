from django.contrib import admin

from .models import Book, Publisher, Author, Genre, Tag, Category


# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Tag)
admin.site.register(Category)
