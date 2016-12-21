from django.shortcuts import render
from django.views.generic import ListView
from .models import Movie, Note, News, Calendar, Category
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import NoteForm, MovieForm, CalendarForm


class MovieList(ListView):
    template_name = 'notes/movie_list.html'
    queryset = Movie.objects.order_by('release_date')
    context_object_name = 'all_movies'

class NoteList(ListView):
    template_name = 'notes/note_list.html'
    queryset = Note.objects.all()
    context_object_name = 'all_notes'



class NewsList(ListView):
    model = News

class CalendarList(ListView):
    model = Calendar
    queryset = Calendar.objects.order_by("date_when")
    context_object_name = 'all_calendar'

class IndexView(ListView):
    template_name = 'notes/index.html'
    context_object_name = 'all_movies'
    queryset = Movie.objects.order_by('release_date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_notes'] = Note.objects.all()
        context['all_calendar'] = Calendar.objects.all()
        # And so on for more models
        return context


class NoteCreate(CreateView):
    form_class = NoteForm
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes:index')


class MovieCreate(CreateView):
    form_class = MovieForm
    template_name = 'notes/movie_form.html'
    success_url = reverse_lazy('notes:index')

class MovieUpdate(UpdateView):
    model = Movie
    fields = ['name', 'release_date', 'imdb_link', 'categories']

class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('notes:index')

class CalendarCreate(CreateView):
    form_class = CalendarForm
    template_name = 'notes/calendar_form.html'
    success_url = reverse_lazy('notes:index')