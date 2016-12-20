
from django.conf.urls import url, include
from . import views
from notes.views import MovieList, NoteList

app_name = 'notes'

urlpatterns = [
    url(r'^/movies/$', MovieList.as_view()),
    url(r'^/notes/$', NoteList.as_view()),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'/movies/add/$', views.MovieCreate.as_view(), name='movie-add'),
    url(r'/notes/add/$', views.NoteCreate.as_view(), name='note-add'),
]
