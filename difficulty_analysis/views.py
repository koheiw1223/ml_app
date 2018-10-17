from django.shortcuts import render
from .models import Vocabulary, Sentence

def index(request):
    return render(request, "difficulty_analysis/index.html")

def difficulty_analysis(request):
    d = {
        'vocabularies': Vocabulary.objects.filter(used_status=True),
    }
    return render(request, "difficulty_analysis/vocabulary_index.html", d)
