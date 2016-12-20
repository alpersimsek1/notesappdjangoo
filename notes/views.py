from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie, Note, News, Calendar, Category
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

class MovieList(ListView):
    template_name = 'notes/movie_list.html'
    queryset = Movie.objects.all()
    context_object_name = 'all_movies'

class NoteList(ListView):
    template_name = 'notes/note_list.html'
    queryset = Note.objects.all()
    context_object_name = 'all_notes'

class NewsList(ListView):
    model = News

class CalendarList(ListView):
    model = Calendar


class IndexView(ListView):
    template_name = 'notes/index.html'
    context_object_name = 'all_movies'
    queryset = Movie.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        context['calendar'] = Calendar.objects.all()
        # And so on for more models
        return context

class MovieCreate(CreateView):
    model = Movie
    fields = ['name', 'release_date', 'imdb_link']
    success_url = reverse_lazy('notes:index')


class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'body', 'created_at']
    success_url = reverse_lazy('notes:index')