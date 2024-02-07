from django.test import TestCase
from django.urls import reverse
from .models import SearchHistory

class WordFrequencyAnalysisTestCase(TestCase):
    def test_word_frequency_analysis_endpoint(self):
        url = reverse('word_frequency_analysis')
        data = {'topic': 'Python programming', 'n': 5}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed

class SearchHistoryTestCase(TestCase):
    def setUp(self):
        SearchHistory.objects.create(topic='Python programming', top_words='Python, programming')

    def test_search_history_endpoint(self):
        url = reverse('search_history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['search_history']), 1)
        # Add more assertions as needed
