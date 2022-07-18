from django import forms


class SearchForm(forms.Form):
    text_search = forms.CharField(max_length=255)