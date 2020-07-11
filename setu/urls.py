from django.contrib import admin
from django.urls import path
from setu.views import index, auth
from search.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('auth', auth, name='auth'),
    path('search', search, name='search'),
]
