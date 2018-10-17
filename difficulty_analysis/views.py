from django.shortcuts import render
from .models import Vocabulary, Sentence

# Create your views here.
def index(request):
    data = {
        'article': Vocabulary.objects.filter(used_status=True),
    }
    return render(request, "difficulty_analysis/vocabulary_index.html", data)