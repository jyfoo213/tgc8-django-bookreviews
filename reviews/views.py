from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from books.models import Book
# Create your views here.


def index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.template.html', {
        'reviews': reviews
    })


@login_required
def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        # fill in the form with what the user has typed in
        form = ReviewForm(request.POST)
        if form.is_valid():
            # save the form it will the create model instance
            # i.e it will insert the new row into the table in the database
            # when we specify Commit=False, means don't save to database directly
            review = form.save(commit=False)
            review.user = request.user  # request.user will contain the currently logged in user
            review.book = book
            review.save()
            messages.success(request, "New review added!")
            return redirect(index)
    else:
        form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            'form': form,
            'book': book
        })
