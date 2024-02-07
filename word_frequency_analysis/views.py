from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import SearchHistory
import wikipediaapi

class WordFrequencyAnalysisView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        topic = request.POST.get('topic')
        n = int(request.POST.get('n', 10))

        wiki_wiki = wikipediaapi.Wikipedia('en')
        page = wiki_wiki.page(topic)
        text = page.text

        # Perform word frequency analysis here
        # Example: Use NLTK or other libraries
        top_words = {'apple': 10, 'banana': 8, 'orange': 6}
        # Store search history
        search_history = SearchHistory.objects.create(topic=topic, top_words=top_words)

        return JsonResponse({'top_words': top_words})

    def get(self, request):
        return JsonResponse({'error': 'GET requests are not supported. Please use POST.'})


class SearchHistoryView(View):
    def get(self, request):
        search_history = SearchHistory.objects.all()
        data = [{'topic': entry.topic, 'top_words': entry.top_words} for entry in search_history]
        return JsonResponse({'search_history': data})

    def post(self, request):
        return JsonResponse({'error': 'POST requests are not supported for this endpoint.'})
