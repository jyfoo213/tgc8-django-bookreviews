from django.urls import path, include
import books.views

urlpatterns = [
    path('', books.views.index),
    path('search/', books.views.search),
    path('book/details/<book_id>', books.views.view_book_details, name="book_details_route"),
    path('book/create', books.views.create_book),
    path('book/edit/<book_id>', books.views.edit_book,
         name='update_book_route'),
    path('book/delete/<book_id>', books.views.delete_book,
         name="delete_book_route"),
    path('authors/', books.views.view_authors),
    path('author/create', books.views.create_author),
    path('author/delete/<author_id>', books.views.delete_author,
         name="delete_author_route"),
    path('author/edit/<author_id>', books.views.edit_author,
         name="update_author_route"),
    path('publishers', books.views.view_publishers),
    path('publisher/create', books.views.create_publisher),
    path('publisher/delete/<publisher_id>', books.views.delete_publisher,
         name="delete_publisher_route")
]