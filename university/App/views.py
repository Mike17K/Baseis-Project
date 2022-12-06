from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewList

# Create your views here.
def index(response):

    form = CreateNewList()
    
    return render(response,"App/base.html",{"form":form})



def create(response):
    if response.method == "POST":

        form = CreateNewList()
        if form.is_valid():
            n=form.clean()
        
        return render(response,"App/Create.html",{"form":form})
