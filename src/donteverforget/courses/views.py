from django.shortcuts import render
from .models import Course
from django.views.generic import ListView, CreateView, DetailView
from .forms import CourseCreateForm

# list view that shows to do list

class CoursesListView(ListView):
    template_name = 'courses/courses_list.html'
    context_object_name = 'courses_list'

    def get_queryset(self):
        return Course.objects.all()


# detail view that shows to do list details

class CoursesDetailView(DetailView):
    template_name = 'courses/courses_detail.html'

    def get_queryset(self):
        return Course.objects.all()

# create view in order to create new courses

class CourseCreateView(CreateView):
    form_class = CourseCreateForm
    template_name = 'courses/courses_create.html'
    success_url = '/courses/'