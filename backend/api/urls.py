from django.urls import path
from . import views

urlpatterns = [
    # Paths for handling quotes
    path("quotes/", views.QuoteListCreate.as_view(), name="quote-list"),
    path("quotes/delete/<int:pk>/", views.QuoteDelete.as_view(), name="delete-quote"),

    # Optional paths for authors, sources, and categories if you have views for these
    path("authors/", views.AuthorList.as_view(), name="author-list"),
    path("authors/<int:pk>/", views.AuthorDetail.as_view(), name="author-detail"),

    path("sources/", views.SourceList.as_view(), name="source-list"),
    path("sources/<int:pk>/", views.SourceDetail.as_view(), name="source-detail"),

    path("categories/", views.CategoryList.as_view(), name="category-list"),
    path("categories/<int:pk>/", views.CategoryDetail.as_view(), name="category-detail"),
]
