"""BookReviewsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import books.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('books/', books.views.index),
    path('book/details/<book_id>', books.views.view_book_details),
    path('book/create', books.views.create_book),
    path('book/edit/<book_id>', books.views.edit_book,
         name='update_book_route'),
    path('book/delete/<book_id>', books.views.delete_book,
         name="delete_book_route"),
    path('reviews/', reviews.views.index),
    path('reviews/create', reviews.views.create_review),
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
