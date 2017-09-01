from .models import Entry
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .forms import EntryCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin

# list view that shows to do list

class ToDoListView(LoginRequiredMixin, ListView):
    template_name = 'todo/entry_list.html'
    context_object_name = 'todo_list'

# gets instances of logged-in user

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

# detail view that shows to do list details

class ToDoDetailView(LoginRequiredMixin, DetailView):
    template_name = 'todo/entry_detail.html'

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

# create view in order to create new entries

class ToDoCreateView(LoginRequiredMixin, CreateView):
    form_class = EntryCreateForm
    template_name = 'todo/entry_create.html'
    success_url = '/todo/'

# ensures that user is logged-in in order to create a new entry

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ToDoCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(ToDoCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)

# delete view in order to delete entries

class ToDoDeleteView(LoginRequiredMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy('todo:list')

# update view in order to edit existing entries

class ToDoUpdateView(LoginRequiredMixin, UpdateView):
    form_class = EntryCreateForm
    template_name = 'todo/entry_update.html'

    def get_queryset(self):
        return Entry.objects.filter(user=self.request.user)  # checks if user is authenticated

    def get_form_kwargs(self):
        kwargs = super(ToDoUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
