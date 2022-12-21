from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewUser,CreateNewMessage,CreateNewAggelia,CreateNewQuery
from .databace_functions import *
import sqlite3

import time
from datetime import datetime

# Create your views here.
def index(request):
    conn =sqlite3.connect('test_databace.db')

    form_user = CreateNewUser()
    form_aggelia = CreateNewAggelia()
    form_message = CreateNewMessage()
    form_query = CreateNewQuery()

    if request.method == 'POST':
        ''' user and company fix
        if 'name' in request.POST.keys():
            # check if the for valid
            isvalid = True

            if isvalid:
                now = datetime.now()
                date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                insert_xristis(conn,request.POST[''],request.POST[''],request.POST[''],date_time_str,request.POST[''],φωτογραφια)
        '''
        if 'zitisi_polisi' in request.POST.keys():
            # check if the for valid
            isvalid = True

            if isvalid:
                now = datetime.now()
                date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                insert_aggelia(conn,0,date_time_str,request.POST['zitisi_polisi']=='z',request.POST['timi'],request.POST['vehicle_type'],request.POST['description'],request.POST['location'],request.POST['vehicle'],request.POST['writer'],5.0,"Pending",request.POST['payment_method'])
            
        if 'message' in request.POST.keys():
            # check if the for valid
            isvalid = True

            if isvalid:
                now = datetime.now()
                date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                insert_minima(conn,date_time_str,'sent',request.POST['message'],request.POST['aggelia'])
             
                
        #form = MyForm(request.POST)
        #if form.is_valid():
         #   pass
            # access cleaned data
            #form_data = form.cleaned_data
            # do something with the data
            # ...
        conn.close()
        
    return render(request,"App/forms.html",{"form_user":form_user,"form_aggelia":form_aggelia,"form_message":form_message,"form_query":form_query})



def create(response):
    if response.method == "POST":

        form = CreateNewUser()
        if form.is_valid():
            n=form.clean()
        
        return render(response,"App/Create.html",{"form":form})
