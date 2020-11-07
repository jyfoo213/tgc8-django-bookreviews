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
from django.urls import path

import books.views
import reviews.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books.views.index),
    path('reviews/', reviews.views.index),
    path('authors/', books.views.view_authors),
    path('create_book/', books.views.create_book),
    path('create_publisher/', books.views.create_publisher),
    path('create_author/', books.views.create_author),
    path('edit_book/<book_id>', books.views.edit_book,
         name='update_book_route'),
    path('edit_author/<author_id>', books.views.edit_author,
         name="update_author_route")
]
