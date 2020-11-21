from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from .models import Book, Author, Publisher
from .forms import BookForm, PublisherForm, AuthorForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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


def view_publishers(request):
    all_publishers = Publisher.objects.all()
    print(all_publishers)
    return render(request, 'books/publishers.template.html', {
        'publishers': all_publishers
    })


@login_required
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
            messages.success(
                request, f'New book {form.cleaned_data["title"]} has been created')
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


def delete_book(request, book_id):
    # check if the form has been submtited via POST
    if request.method == "POST":
        book_being_deleted = get_object_or_404(Book, pk=book_id)
        book_being_deleted.delete()
        return redirect(index)
    else:
        # if the form haven't been submitted via POST, then it means it is via GET
        # hence we display the form
        book_being_deleted = get_object_or_404(Book, pk=book_id)
        return render(request, 'books/confirm_delete.template.html', {
            'book': book_being_deleted
        })


def delete_publisher(request, publisher_id):
    if request.method == "POST":
        publisher_to_delete = get_object_or_404(Publisher, pk=publisher_id)
        publisher_to_delete.delete()
        return redirect(view_publishers)
    else:
        publisher_to_delete = get_object_or_404(Publisher, pk=publisher_id)
        return render(request, 'books/confirm_delete_publisher.template.html', {
            'publisher': publisher_to_delete
        })


def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        author.delete()
        return redirect(view_authors)
    else:
        return render(request, 'books/confirm_delete_author.template.html', {
            'author': author
        })
