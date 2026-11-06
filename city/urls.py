
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('facts/', views.facts, name='facts'),
    path('contacts/', views.contacts, name='contacts'),
    path('history/', views.history, name='history'),
    path('history/people/', views.people, name='people'),
    path('history/photos/', views.photos, name='photos'),
]
