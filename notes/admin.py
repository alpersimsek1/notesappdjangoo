from django.contrib import admin
from .models import Movie, Note, Category, Calendar, News
# Register your models here.
admin.site.register(Movie)
admin.site.register(Note)
admin.site.register(Category)
admin.site.register(
    Calendar
)
admin.site.register(News)