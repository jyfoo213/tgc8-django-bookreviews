from django.shortcuts import render, get_object_or_404, redirect, reverse
from books.models import Book

# Create your views here.


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    # initialize the shopping cart if it does not exist
    # or fetch the cart if it does
    cart = request.session.get('shopping_cart', {})

    # the book is not in the shopping cart
    if book_id not in cart:
        cart[book_id] = {
            'id': book_id,
            'title': book.title,
            'cost': 99,
            'qty': 1
        }
    else:
        # if the shopping cart already has the book,
        # then we assume the user want to buy an additional copy
        cart[book_id]['qty'] += 1

    request.session['shopping_cart'] = cart
    return redirect(reverse('view_books_route'))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})
    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })