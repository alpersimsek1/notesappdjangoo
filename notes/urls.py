
from django.conf.urls import url, include
from . import views
from notes.views import MovieList, NoteList, CalendarList

app_name = 'notes'

urlpatterns = [
    url(r'^movies/$', MovieList.as_view()),
    url(r'^notes/$', NoteList.as_view()),
    url(r'^calendar/$', CalendarList.as_view()),
    url(r'^calendar/add/$', views.CalendarCreate.as_view(), name='calendar-add'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'movies/add/$', views.MovieCreate.as_view(), name='movie-add'),
    url(r'notes/add/$', views.NoteCreate.as_view(), name='note-add'),
    url(r'movies/(?P<pk>[0-9]+)/$', views.MovieUpdate.as_view(), name='movie-update'),
        # music/album/2/delete
    url(r'movies/(?P<pk>[0-9]+)/delete/$', views.MovieDelete.as_view(), name='movie-delete'),

]
