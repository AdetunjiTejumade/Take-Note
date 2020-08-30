from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import (
            ListView, 
            DetailView, 
            TemplateView
    )
from django.views.generic.edit import (
    UpdateView,
    DeleteView,
    CreateView
)

from django.urls import reverse_lazy
from .models import Note
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html" 

class NoteListView(LoginRequiredMixin, ListView):
    context_object_name = "notes"
    template_name = 'note_list.html'
    login_url = 'login'

    
    def get_queryset(self):
        return Note.objects.filter(author=self.request.user)
    
class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note
    context_object_name = 'note_detail'
    template_name = 'note_detail.html'
    login_url = 'login'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    template_name = 'new_note.html'
    fields = ['title', 'body'] # Specifies field to be displayed
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    template_name = 'update_note.html'
    fields = ['title', 'body']
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()      
        return obj.author == self.request.user

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = 'delete_note.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()      
        return obj.author == self.request.user