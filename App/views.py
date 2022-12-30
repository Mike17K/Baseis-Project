from asyncio.windows_events import NULL
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewUserIdiotis,CreateNewUserCompany,CreateNewMessage,CreateNewAggelia,CreateNewQuery
from .databace_functions import *
import sqlite3

import time
from datetime import datetime

# Create your views here.
def index(request):
    conn =sqlite3.connect('test_databace.db')
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT id, email FROM χρηστης;') #  join idiotis on χρηστης.id=idiotis.id') # θελω και τις επιχειρησεις εδω 
    USER_CHOICES = [(row[0], row[1]) for row in cursor.fetchall()]

    cursor.execute('SELECT DISTINCT id,τιτλος FROM αγγελία;') #  join idiotis on χρηστης.id=idiotis.id') # θελω και τις επιχειρησεις εδω 
    AGGELIA_CHOICES = [(row[0], row[1]) for row in cursor.fetchall()]

    cursor.execute('SELECT DISTINCT id,πολη,νομός,χώρα FROM περιοχη;') #  join idiotis on χρηστης.id=idiotis.id') # θελω και τις επιχειρησεις εδω 
    LOCATION_CHOICES = [(row[0], row[1]+','+row[2]+','+row[3]) for row in cursor.fetchall()]

    cursor.execute('SELECT DISTINCT id,κατηγορία,μαρκα,πινακιδα FROM οχημα;') #  join idiotis on χρηστης.id=idiotis.id') # θελω και τις επιχειρησεις εδω 
    VEHICLE_CHOICES = [(row[0], row[1]+','+row[2]+','+row[3]) for row in cursor.fetchall()]

    WRITER_CHOICES = [i for i in USER_CHOICES]

    form_user_idiotis = CreateNewUserIdiotis()
    form_user_company = CreateNewUserCompany()
    form_aggelia = CreateNewAggelia(request.POST,
        location_new_choices=LOCATION_CHOICES,
        vehicle_new_choices=VEHICLE_CHOICES,
        writer_new_choices=USER_CHOICES
        )
    
    form_message = CreateNewMessage(request.POST,
        aggelia_new_choices=AGGELIA_CHOICES,
        sender_new_choices=WRITER_CHOICES
        )
    form_query = CreateNewQuery()
    query_results = []
    query = ''

    if request.method == 'POST':
        # user and company fix
        if 'email' in request.POST.keys():
            # check if the for valid
            isvalid = True

            if 'firstname' in request.POST.keys():
                cursor.execute(f"SELECT id FROM χρηστης where ΑΦΜ={request.POST['AFM']};") 
                isvalid = isvalid and len(cursor.fetchall()) == 0
                if not isvalid: print("Error AFM already exists") # show to screen the message
                
                cursor.execute(f"SELECT DISTINCT id FROM χρηστης where email='{request.POST['email']}';") 
                isvalid = isvalid and len(cursor.fetchall()) == 0
                if not isvalid: print("Error email already exists") # show to screen the message

                cursor.execute(f"SELECT DISTINCT id FROM χρηστης where τηλ={request.POST['phone']};") 
                isvalid = isvalid and len(cursor.fetchall()) == 0
                if not isvalid: print("Error phone already exists") # show to screen the message
                
            # company checks
            if 'company_name' in request.POST.keys():
                cursor.execute(f"SELECT id FROM επιχειρηση where επωνυμια='{request.POST['company_name']}';") 
                isvalid = isvalid and len(cursor.fetchall()) == 0
                if not isvalid: print("Error comopany name already exists") # show to screen the message
                
                cursor.execute(f"SELECT DISTINCT id FROM επιχειρηση where site='{request.POST['site']}';") 
                isvalid = isvalid and len(cursor.fetchall()) == 0
                if not isvalid: print("Error site already exists") # show to screen the message
            

            if isvalid:
                now = datetime.now()
                date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                
                insert_xristis(conn,request.POST['address'],request.POST['AFM'],request.POST['email'],date_time_str,request.POST['phone'],"0")
                # find xristis id
                cursor.execute(f"SELECT DISTINCT id FROM χρηστης where ΑΦΜ={request.POST['AFM']};") #  join idiotis on χρηστης.id=idiotis.id') # θελω και τις επιχειρησεις εδω 
                uid = int(cursor.fetchall()[0][0])
                if 'firstname' in request.POST.keys():
                    insert_idiotis(conn,uid,request.POST['firstname'],request.POST['lastname'])
                elif 'company_name' in request.POST.keys():
                    insert_company(conn,uid,request.POST['site'],request.POST['company_name'],request.POST['business_type'])
                else: print("ERROR")
                
                    

        if 'zitisi_polisi' in request.POST.keys():
            # check if the for valid
            isvalid = True
            
            cursor.execute(f"SELECT id FROM αγγελία where τιτλος={request.POST['titlos']};") 
            isvalid = isvalid and len(cursor.fetchall()) == 0
            if not isvalid: print("Error titlos already exists") # show to screen the message
            
            if isvalid:
                now = datetime.now()
                date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                insert_aggelia(conn,0,date_time_str,request.POST['zitisi_polisi']=='z',request.POST['timi'],request.POST['vehicle_type'],request.POST['titlos'],request.POST['description'],request.POST['location'],request.POST['vehicle'],request.POST['writer'],5.0,"Pending",request.POST['payment_method'])

        if 'message' in request.POST.keys():
            # check if the for valid
            isvalid = True

            # ο συντακτης δε μπορει να στειλει μυνημα σε αγγελία που του ανοικει
            now = datetime.now()
            date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            insert_minima(conn,request.POST['sender'],date_time_str,'sent',request.POST['message'],request.POST['aggelia'])
            
            cursor.execute(f"""select συντακτης from αγγελία as A where A.id={request.POST['aggelia']}""")
            uid = int(cursor.fetchall()[0][0])
            
            cursor.execute(f"""select id from μηνυμα where αφορα={request.POST['aggelia']}""")
            message_id = int(cursor.fetchall()[0][0])
            
            isvalid = isvalid and uid!=int(request.POST['sender'])
            if not isvalid: print("U cant send message to yourself")

            if isvalid:    
                insert_aposteli(conn,request.POST['sender'],uid,message_id) ############### ADD
        
        if 'my_query' in request.POST.keys():
            # check if the for valid
            isvalid = True

            if isvalid:
                now = datetime.now()
                date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
                try:
                    cursor.execute(f"{request.POST['my_query']}")
                    query = request.POST['my_query']
                    query_results = cursor.fetchall()
                except:
                    query = ''
                
        conn.close()
        
    return render(request,"App/forms.html",{"form_user_company":form_user_company,"form_user_idiotis":form_user_idiotis,"form_aggelia":form_aggelia,"form_message":form_message,"form_query":form_query,"query_results":query_results,"query":query})

