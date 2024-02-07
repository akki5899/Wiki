from django.urls import path
from . import views

urlpatterns = [
    path('word-frequency-analysis/', views.WordFrequencyAnalysisView.as_view(), name='word_frequency_analysis'),
    path('search-history/', views.SearchHistoryView.as_view(), name='search_history'),
]
