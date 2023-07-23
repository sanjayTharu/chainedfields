from django.shortcuts import render
from dal import autocomplete
from .models import Category

# Create your views here.

class CategoryAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Category.objects.none()
        
        brand=self.forwarded.get('brand',None)
        if brand:
            qs=Category.objects.filter(brand=brand)
        else:
            qs=Category.objects.none()

        if self.q:
            qs=qs.filter(name__istartwith=self.q)
        return qs
    
