from django.conf.urls import url
from .views import (
    CoursesListView,
    CoursesDetailView,
    CourseCreateView
)

urlpatterns = [
    url(r'^create/$', CourseCreateView.as_view(), name='create'),
    url(r'^$', CoursesListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', CoursesDetailView.as_view(), name='detail'),
]