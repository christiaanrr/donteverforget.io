from django.conf.urls import url
from .views import (
    ToDoListView,
    ToDoDetailView,
)

urlpatterns = [
    url(r'^$', ToDoListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ToDoDetailView.as_view(), name='detail'),
]