from django.conf.urls import url
from .views import (
    CoursesListView,
    CoursesDetailView,
)

urlpatterns = [
    url(r'^$', CoursesListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', CoursesDetailView.as_view(), name='detail'),
]