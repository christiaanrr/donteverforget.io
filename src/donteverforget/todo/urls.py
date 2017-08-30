from django.conf.urls import url
from .views import (
    ToDoListView,
    ToDoDetailView,
    ToDoCreateView,
)

urlpatterns = [
    url(r'^create/$', ToDoCreateView.as_view(), name='create'),
    url(r'^$', ToDoListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ToDoDetailView.as_view(), name='detail'),
]