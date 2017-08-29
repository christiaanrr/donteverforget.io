from django.shortcuts import render
from .models import Course
from django.views.generic import ListView, CreateView, DetailView

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