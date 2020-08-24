from django.urls import path
from .views import (
        NoteListView, 
        NoteCreateView, 
        NoteDetailView, 
        NoteUpdateView,
        NoteDeleteView
    )
urlpatterns = [
    path('', NoteListView.as_view(), name="home"), # Home Page
    path('note/<int:pk>', NoteDetailView.as_view(), name="note_detail"), # Url for detailed note view
    path('note/new', NoteCreateView.as_view(), name="new_note"), # Url for creating new notes
    path('note/<int:pk>/edit/', NoteUpdateView.as_view(), name="update_note"), # Update note url | note/pk/edit
    path('note/<int:pk>/delete/', NoteDeleteView.as_view(), name="delete_note"),
]