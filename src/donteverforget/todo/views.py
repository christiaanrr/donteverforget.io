from django.shortcuts import render
from .models import Entry
from django.views.generic import ListView, CreateView, DetailView

# list view that shows to do list

class ToDoListView(ListView):
    template_name = 'todo/entry_list.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Entry.objects.all()

# detail view that shows to do list details

class ToDoDetailView(DetailView):
    template_name = 'todo/entry_detail.html'

    def get_queryset(self):
        return Entry.objects.all()
