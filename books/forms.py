from django import forms
from .models import Book, Publisher, Author, Genre, Tag
from cloudinary.forms import CloudinaryJsFileField


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')
    cover = CloudinaryJsFileField()


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'email', 'website')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob')


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    genre = forms.ModelChoiceField(
        queryset=Genre.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False)
