from django.forms import ModelForm, Textarea, URLField, SelectDateWidget, SplitHiddenDateTimeWidget
from django.forms.extras.widgets import SelectDateWidget
from .models import Movie, Note, Calendar
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'release_date', 'imdb_link', 'categories']
        widgets = {
            'release_date': SelectDateWidget,
        }

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body', 'created_at', 'categories']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),

        }

class CalendarForm(ModelForm):
    class Meta:
        model = Calendar
        fields = ['title', 'date_when']
        widgets = {
            'date_when': SelectDateWidget,
        }

