from django.conf.urls import url
from .views import (
    ToDoListView,
    ToDoDetailView,
    ToDoCreateView,
    ToDoDeleteView,
    ToDoUpdateView
)

urlpatterns = [
    url(r'^create/$', ToDoCreateView.as_view(), name='create'),
    url(r'^$', ToDoListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ToDoDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', ToDoUpdateView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+)/delete/$', ToDoDeleteView.as_view(), name='delete'),
]