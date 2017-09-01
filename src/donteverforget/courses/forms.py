from django import forms
from .models import Course

class CourseCreateForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = [
            'course',
            'subject',
            'term',
            'description'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 25}),
        }