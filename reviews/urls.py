from django.urls import path, include
import reviews.views
urlpatterns = [
    path('', reviews.views.index),
    path('create/<book_id>', reviews.views.create_review, name="create_review_route"),
]