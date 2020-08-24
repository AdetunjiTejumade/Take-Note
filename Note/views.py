from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
            ListView, 
            CreateView, 
            DetailView, 
            UpdateView, 
            DeleteView,
    )
from django.urls import reverse_lazy
from .models import Note
# Create your views here.

class NoteListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = 'note_list.html'

class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note_detail'
    template_name = 'note_detail.html'

class NoteCreateView(CreateView):
    model = Note
    template_name = 'new_note.html'
    fields = ['body'] # Specifies field to be displayed

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'update_note.html'
    fields = ['body']

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'delete_note.html'
    success_url = reverse_lazy('home')
