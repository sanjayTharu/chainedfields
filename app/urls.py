from django.urls import path
from .views import CategoryAutocompleteView


urlpatterns=[
    path('category-autocomplete/',CategoryAutocompleteView.as_view(),name='category_autocomplete'),
]