from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vocabularies/', views.difficulty_analysis, name='vocabularies'),
]
