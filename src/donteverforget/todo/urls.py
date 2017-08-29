from django.conf.urls import url
from .views import (
    ToDoListView,
)

urlpatterns = [
    url(r'^$', ToDoListView.as_view(), name='list')
]