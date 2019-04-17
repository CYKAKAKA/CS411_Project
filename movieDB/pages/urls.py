from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('movie/', views.movie, name = 'movie'),
    path('director/', views.director, name = 'director'),
    path('actor/', views.actor, name = 'actor'),
    path('prediction/', views.prediction, name = 'prediction'),
    path('recommendation/', views.recommendation, name = 'recommendation'),
    path('insert_data/', views.insert_data, name = 'insert_data'),
    path('insert_data_submission/', views.insert_data_submission, name = 'insert_data_submission'),
    path('new_movie/', views.new_movie, name='new_movie'),
    url(r'^edit_movie/(?P<pk>\d+)/$', views.edit_movie, name='edit_movie'),
    url(r'^delete_movie/(?P<pk>\d+)/$', views.delete_movie, name='delete_movie'),
<<<<<<< HEAD
    url(r'^result/$', views.search, name='search'),
    url(r'^movie_detail/(?P<id>\d+/$)', views.detail, {'model': models.Movie}, name='movie_detail')
=======
    url(r'^recommedation/$', views.search, name='search'),
>>>>>>> c30c8416828bd9e8cf4bbc209430bc919d2e36c7
]