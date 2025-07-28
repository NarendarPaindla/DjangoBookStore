from django.urls import path
from .views import BooksListView,BookDetailView
urlpatterns=[
    path("",BooksListView.as_view(),name="list"),
    path("<int:pk>",BookDetailView.as_view(),name="detail"),
]