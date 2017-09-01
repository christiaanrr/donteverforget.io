from django import forms
from .models import Entry
from courses.models import Course

class EntryCreateForm(forms.ModelForm):

    def __init__(self, user=None, *args, **kwargs):
        super(EntryCreateForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.filter(owner=user)

    class Meta:
        model = Entry
        fields = [
            'title',
            'course',
            'due_date',
            'description'
        ]