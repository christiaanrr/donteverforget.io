from django.shortcuts import render
from .models import Entry
from django.views.generic import ListView
# list view that shows to do list

class ToDoListView(ListView):
    template_name = 'todo/entry_list.html'
    def get_queryset(self):
        return Entry.objects.all()