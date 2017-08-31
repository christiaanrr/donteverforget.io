from django.shortcuts import render
from .models import Entry
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import EntryCreateForm

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

# create view in order to create new entries

class ToDoCreateView(CreateView):
    form_class = EntryCreateForm
    template_name = 'todo/entry_create.html'
    success_url = '/todo/'

# delete view in order to delete entries

class ToDoDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('todo:list')

# update view in order to edit existing entries

class ToDoUpdateView(UpdateView):
    form_class = EntryCreateForm
    template_name = 'todo/entry_update.html'

    def get_queryset(self):
        return Entry.objects.all()