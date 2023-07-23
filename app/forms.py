from django import forms
from .models import Category,Product
from dal import autocomplete

class ProductForm(forms.ModelForm):
    category=forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='category_autocomplete',
            forward=['brand']
        )
    )

    class Meta:
        model=Product
        fields='__all__'
        