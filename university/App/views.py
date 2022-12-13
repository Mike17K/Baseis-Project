from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewUser,CreateNewMessage,CreateNewAggelia,CreateNewQuery


# Create your views here.
def index(response):

    form_user = CreateNewUser()
    form_aggelia = CreateNewAggelia()
    form_message = CreateNewMessage()
    form_query = CreateNewQuery()

    return render(response,"App/forms.html",{"form_user":form_user,"form_aggelia":form_aggelia,"form_message":form_message,"form_query":form_query})



def create(response):
    if response.method == "POST":

        form = CreateNewUser()
        if form.is_valid():
            n=form.clean()
        
        return render(response,"App/Create.html",{"form":form})
