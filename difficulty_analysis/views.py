from django.shortcuts import render
from .models import Vocabulary, Sentence

def index(request):
    return render(request, "difficulty_analysis/index.html")

def vocabulary_index(request):
    d = {
        'vocabularies': Vocabulary.objects.filter(used_status=True),
    }
    return render(request, "difficulty_analysis/vocabulary_index.html", d)

def sentence_index(request):
    d = {
        'sentences': Sentence.objects.filter(used_status=True),
    }
    return render(request, "difficulty_analysis/sentence_index.html", d)