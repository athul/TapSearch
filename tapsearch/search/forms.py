from django import forms
class searchForm(forms.Form):
    searchQuery=forms.CharField(max_length=50, required=True)
