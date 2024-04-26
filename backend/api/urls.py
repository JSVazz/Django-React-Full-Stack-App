from django.urls import path
from .views import (
    QuoteListCreate, QuoteDetail, QuoteDelete, 
    AuthorListCreate, AuthorDetail,
    SourceListCreate, SourceDetail,
    CategoryListCreate, CategoryDetail
)

urlpatterns = [
    path("quotes/", QuoteListCreate.as_view(), name="quote-list"),
    path("quotes/<int:pk>/", QuoteDetail.as_view(), name="quote-detail"),
    path("quotes/delete/<int:pk>/", QuoteDelete.as_view(), name="delete-quote"),
    path("authors/", AuthorListCreate.as_view(), name="author-list"),
    path("authors/<int:pk>/", AuthorDetail.as_view(), name="author-detail"),
    path("sources/", SourceListCreate.as_view(), name="source-list"),
    path("sources/<int:pk>/", SourceDetail.as_view(), name="source-detail"),
    path("categories/", CategoryListCreate.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
]
