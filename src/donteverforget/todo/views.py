from django.shortcuts import render
from .models import Entry
from django.views.generic import ListView, CreateView, DetailView
# list view that shows to do list

class ToDoListView(ListView):
    template_name = 'todo/entry_list.html'
    def get_queryset(self):
        return Entry.objects.all()

class ToDoDetailView(DetailView):
    template_name = 'todo/entry_detail.html'
    def get_queryset(self):
        return Entry.objects.all()