from django.shortcuts import render
from .models import Course
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseCreateForm

# list view that shows to do list

class CoursesListView(LoginRequiredMixin, ListView):
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses_list'

# displays logged in user's instances
    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)


# detail view that shows to do list details

class CoursesDetailView(LoginRequiredMixin, DetailView):
    template_name = 'courses/courses_detail.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)

# create view in order to create new courses

class CoursesCreateView(LoginRequiredMixin, CreateView):
    form_class = CourseCreateForm
    template_name = 'courses/courses_create.html'
    success_url = '/courses/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(CoursesCreateView, self).form_valid(form)

# delete view in order to delete entries

class CoursesDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')

# update view in order to edit existing entries

class CoursesUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CourseCreateForm
    template_name = 'courses/courses_update.html'

    def get_queryset(self):
        return Course.objects.filter(owner=self.request.user)
