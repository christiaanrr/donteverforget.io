from django.conf.urls import url
from .views import (
    CoursesListView,
    CoursesDetailView,
    CoursesCreateView,
    CoursesDeleteView,
    CoursesUpdateView
)

urlpatterns = [
    url(r'^create/$', CoursesCreateView.as_view(), name='create'),
    url(r'^$', CoursesListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', CoursesDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', CoursesUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', CoursesDeleteView.as_view(), name='delete'),
]