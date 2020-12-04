import markdown2
from django import forms
from django.shortcuts import render

from . import util

class SearchForm(forms.Form):
    query = forms.CharField(label="Search",
        widget = forms.TextInput(attrs={'placeholder': 'Search Wiki',
        'style': 'width:100%'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form": SearchForm
    })

def get_page(request, title):
    #get the contents of the page from util.py
    page = util.get_entry(title)
    #check if page exists or not
    if page is None:
        return render(request, "encyclopedia/error.html", {
            "error": "The requested page was not found",
            "form": SearchForm
        })
    #display the contents of the page.
    else:
        return render(request, "encyclopedia/title.html", {
            "title": title,
            #convert markdown content to html
            "content": markdown2.markdown(page),
            "form": SearchForm
        })

def search(request):
    return render(request, "encyclopedia/search.html", {
        "form": SearchForm
    })
