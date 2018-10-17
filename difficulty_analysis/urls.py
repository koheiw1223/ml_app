from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vocabularies/', views.vocabulary_index, name='vocabularies'),
    path('sentences/', views.sentence_index, name='sentences'),
]
