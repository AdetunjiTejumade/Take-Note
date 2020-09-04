from django.contrib import admin

from .models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('author', 'title',)}

admin.site.register(Note, NoteAdmin)