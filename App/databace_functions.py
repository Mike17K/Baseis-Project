import sqlite3
import os
import random
import string
from django import forms

conn =sqlite3.connect('test_databace.db')


def insert_xristis(conn,διευθυσνη,ΑΦΜ,email,ημερομηνια,τηλ,φωτογραφια):
    try:
        cur =conn.cursor()

        cur.execute(f""" INSERT INTO χρηστης (διευθυσνη,ΑΦΜ,email,ημερομηνια,τηλ,φωτογραφια) VALUES 
                ('{διευθυσνη}',{ΑΦΜ},'{email}','{ημερομηνια}',{τηλ},{φωτογραφια});""")
        conn.commit()
    except :
        return -1
    return 0

def insert_idiotis(conn,id,name,surname):
    try:
        cur =conn.cursor()

        cur.execute(f""" INSERT INTO idiotis (id,name,surname) VALUES ({id},'{name}','{surname}');""")
        conn.commit()
    except AttributeError as e:
        print(e)
        return -1
    return 0

def insert_company(conn,id,site,επωνυμια,τυπος):
    try:
        cur =conn.cursor()

        cur.execute(f""" INSERT INTO επιχειρηση (id,site,επωνυμια,τυπος) VALUES 
                ({id},'{site}','{επωνυμια}','{τυπος}');""")
        conn.commit()
    except AttributeError as e:
        print(e)
        return -1
    return 0

def insert_aggelia(conn,εμφανισεις,ημερομηνια,ζητηση_πωληση,τιμη,τυπος,τιτλος,περιγραφη,περιοχη,οχημα,συντακτης,ποσο,κατασταση,τροπος):
    try:
        cur =conn.cursor()

        cur.execute(f""" INSERT INTO αγγελία (εμφανισεις,ημερομηνια,ζητηση_πωληση,τιμη,
        τυπος,τιτλος,περιγραφη,περιοχη,οχημα,συντακτης,ποσο,κατασταση,τροπος) VALUES 
                ({εμφανισεις},'{ημερομηνια}',{ζητηση_πωληση},{τιμη},'{τυπος}','{τιτλος}',
                '{περιγραφη}','{περιοχη}','{οχημα}',{συντακτης},{ποσο},'{κατασταση}','{τροπος}');""")
        conn.commit()
    except AttributeError as e:
        print(e)
        return -1
    return 0
    
def insert_minima(conn,συντακτης,ημερομηνια,κατασταση,κειμενο,αφορα):
    try:
        cur =conn.cursor()
        cur.execute(f""" INSERT INTO μηνυμα (συντακτης,ημερομηνια,κατασταση,κειμενο,αφορα) VALUES 
                ({συντακτης},'{ημερομηνια}','{κατασταση}','{κειμενο}',{αφορα});""")
        conn.commit()
    except AttributeError as e:
        print(e)
        return -1
    return 0

def insert_aposteli(conn,αποστολεας,παραληπτης,μηνυμα):
    try:
        cur =conn.cursor()
        cur.execute(f""" INSERT INTO αποστελει (αποστολεας,παραληπτης,μηνυμα) VALUES 
                ({αποστολεας},{παραληπτης},{μηνυμα});""")
        conn.commit()
    except AttributeError as e:
        print(e)
        return -1
    return 0

def insert_perioxh(conn,ΤΚ,πολη,γεωγραφικες_συντεταγμενες,νομός,χώρα):
    try:
        cur =conn.cursor()
        cur.execute(f""" INSERT INTO περιοχη (ΤΚ,πολη,γεωγραφικες_συντεταγμενες,νομός,χώρα) VALUES 
                ('{ΤΚ}','{πολη}','{γεωγραφικες_συντεταγμενες}','{νομός}','{χώρα}');""")
        conn.commit()
    except AttributeError as e:
        print(e)
        return -1
    return 0

def insert_vehicles(conn,πορτες,καθισματα,χρώμα,αερόσακοι,κυβικά,ιπποι,μεγεθος,κινηση,καύσιμα,χρονολογία,σαζμαν,πινακιδα,χιλιομετρα,κατηγορία,μαρκα,κατασταση):
    try:
        cur =conn.cursor()
        cur.execute(f""" INSERT INTO οχημα (πορτες,καθισματα,χρώμα,αερόσακοι,κυβικά,ιπποι,μεγεθος,κινηση,καύσιμα,χρονολογία,σαζμαν,πινακιδα,χιλιομετρα,κατηγορία,μαρκα,κατασταση) VALUES 
                ('{πορτες}','{καθισματα}','{χρώμα}','{αερόσακοι}','{κυβικά}','{ιπποι}','{μεγεθος}','{κινηση}','{καύσιμα}','{χρονολογία}','{σαζμαν}','{πινακιδα}','{χιλιομετρα}','{κατηγορία}','{μαρκα}','{κατασταση}');""")
        conn.commit()
    except AttributeError as e:
        print(e)
        return -1
    return 0

def update_vehicles(conn):
    colorlist=['κοκκινο','κιτρινο','μαυρο','μπλε','ασημι']
    category=['αυτοκινητο','μηχανακι','βαν','φορτηγο']
    brands=['audi','mazda','mercedes','bmw','fiat','opel','toyota','tesla']
    letters = string.ascii_uppercase
    pinakida=[]
    for j in range(0,80):
        pinakida.append(random.choice(letters)+random.choice(letters)+random.choice(letters)+'-'+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1)))
    for i in range(0,20):
            insert_vehicles(conn,random.choice([2, 4, 8]),random.choice([2, 4, 6, 8]),random.choice(colorlist),random.choice([2, 4]),random.choice([1000, 1200, 1400, 1600,2000,2200]),
            random.choice([3000, 4000, 5000, 5500]),random.choice([20.2, 14.4, 21.6, 27.8]),random.choice(['χειροκίνητο','αυτόματο']),
            random.choice(['βενζίνη','πετρέλαιο','ηλεκτρικό','αέριο']),random.randrange(1980,2022,1),random.choice(['μηχανικό','αυτόματο']),
            random.choice(pinakida),random.randrange(0,100000,1000),random.choice(category),random.choice(brands),random.choice(['καινουργιο','μεταχειρισμένο']))

def update_areas(conn):
    #Regions=['Στερεα Ελλάδα',"Πελοπόννησος",'Ηπειρος','Κρητη','Θρακη','Δυτική Ελλάδα','Επτάνησα']
    Pre=['Αττικής','Αχαιας','Ιωαννινων','Χανίων','Ξάνθης','Αιτωλοακαρνανίας','Αργοστολίου']
    City=['Αθηνα','Πάτρα','Ιωάννινα','Χανιά','Ξάνθη','Αγρίνιο','Κεφαλονιά']
    TK=[]
    Coord=[]
    for i in range (0,7):
        TK.append(str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1)))
    for i in range(0,7):
        Coord.append(str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+'N  '+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+str(random.randrange(0,9,1))+'W')
    for j in range (0,7):
        insert_perioxh(conn,TK[j],City[j],Coord[j],Pre[j],'Ελλάδα')

def refresh(filename):
    con =sqlite3.connect(filename)
    cur =con.cursor()
    b="""
    DROP TABLE χρηστης;
    DROP TABLE αγγελία;
    DROP TABLE μηνυμα;
    DROP TABLE ανηκει;
    DROP TABLE οχημα;
    DROP TABLE αποστελει;
    DROP TABLE επιχειρηση;
    DROP TABLE idiotis;
    
    """
    t=b.split(";")
    for i in t: 
        cur.execute(i)
    
    a="""
    
CREATE TABLE χρηστης (
    id integer PRIMARY KEY AUTOINCREMENT,
    διευθυσνη string,
    ΑΦΜ integer,
    email string,
    ημερομηνια εγγραφης date,
    τηλ integer,
    φωτογραφια integer
);

CREATE TABLE αγγελία (
    id integer PRIMARY KEY AUTOINCREMENT,
    εμφανισεις integer,
    ημερομηνια date,
    ζητηση_πωληση boolean,
    τιμη float,
    τυπος οχηματος string,
    τιτλος string,
    περιγραφη text,
    περιοχη integer,
    οχημα integer,
    συντακτης integer,
    ποσο χρεωσης float,
    κατασταση χρεωσης string,
    τροπος πληρωμης string
);

CREATE TABLE περιοχη (
    id integer PRIMARY KEY AUTOINCREMENT,
    ΤΚ integer,
    πολη string,
    γεωγραφικες_συντεταγμενες string,
    νομός string,
    χώρα string
);

CREATE TABLE οχημα (
    id integer PRIMARY KEY AUTOINCREMENT,
    πορτες integer,
    καθισματα integer,
    χρώμα string,
    αερόσακοι integer,
    κυβικά integer,
    ιπποι integer,
    μεγεθος ζαντας float,
    κινηση string,
    καύσιμα string,
    χρονολογία date,
    σαζμαν string,
    πινακιδα string,
    χιλιομετρα integer,
    κατηγορία string,
    μαρκα string,
    κατασταση string
);


CREATE TABLE idiotis (
    id integer ,
    name string,
    surname string
);

CREATE TABLE επιχειρηση (
    id integer,
    site string,
    επωνυμια string,
    τυπος επιχειρησης string
);

CREATE TABLE μηνυμα (
    id integer PRIMARY KEY AUTOINCREMENT,
    συντακτης integer,
    ημερομηνια date,
    κατασταση string,
    κειμενο text,
    αφορα integer
);

CREATE TABLE αποστελει (
    id integer PRIMARY KEY AUTOINCREMENT,
    αποστολεας id integer,
    παραληπτης id integer,
    μηνυμα id integer
);

    """
    temp=a.split(";")
    for i in temp: 
        cur.execute(i)

    update_vehicles(con)
    update_areas(con)
    
    con.close()

if __name__ == "__main__":
    
    refresh('test_databace.db')
    conn =sqlite3.connect('test_databace.db')
