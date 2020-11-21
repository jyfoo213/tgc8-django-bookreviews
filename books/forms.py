from django import forms
from .models import Book, Publisher, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'email', 'website')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob')
