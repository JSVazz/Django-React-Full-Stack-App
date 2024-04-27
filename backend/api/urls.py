from django.urls import path
from . import views

urlpatterns = [
    path("quotes/", views.QuoteListCreate.as_view(), name="quote-list"),
    path("quotes/delete/<int:pk>/", views.QuoteDelete.as_view(), name="delete-quote"),
    
]
