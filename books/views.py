from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Author
from .forms import BookForm, PublisherForm, AuthorForm
# Create your views here.


def index(request):
    # eqv. SELECT * FROM books
    all_books = Book.objects.all()
    return render(request, 'books/index.template.html', {
        'books': all_books
    })


def view_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'books/authors.template.html', {
        'authors': all_authors
    })


def create_book(request):
    if request.method == "POST":
        # eqv. request.POST is the same request.form in Flask
        # create the form again but pass in all the user's data
        # that has been submitted
        form = BookForm(request.POST)
        if form.is_valid():
            # actually saving the user's keyed in data to the database
            form.save()
            # eqv. to 'redirect(url_for(index))' in Flask
            return redirect(reverse(index))
    else:
        # create an instance of the BookForm
        create_book_form = BookForm()
        return render(request, 'books/create_book.template.html', {
            'form': create_book_form
        })


def create_publisher(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Publisher added')
    else:
        form = PublisherForm()
        return render(request, 'books/create_publisher.template.html', {
            'form': form
        })


def create_author(request):
    if request.method == "POST":
        # request.POST contains all the data the user has submitted
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(view_authors))
    else:
        author_form = AuthorForm()
        return render(request, 'books/create_author.template.html', {
            'form': author_form
        })


def edit_book(request, book_id):
    book_being_updated = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book_being_updated)
        if form.is_valid():
            form.save()
            return redirect(reverse(index))
    else:

        book_form = BookForm(instance=book_being_updated)
        return render(request, 'books/edit_book.template.html', {
            'form': book_form,
            'book': book_being_updated
        })


def edit_author(request, author_id):
    author_being_updated = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        # the instance argument tells the form which specific author to update
        form = AuthorForm(request.POST, instance=author_being_updated)
        if form.is_valid():
            form.save()
            return redirect(reverse(view_authors))
    else:

        author_form = AuthorForm(instance=author_being_updated)
        return render(request, 'books/edit_author.template.html', {
            'form': author_form,
            'author': author_being_updated
        })
