import sqlite3
import os

conn =sqlite3.connect('test_databace.db')

def insert_xristis(conn,id,διευθυσνη,ΑΦΜ,email,ημερομηνια,τηλ,φωτογραφια):
    try:
        cur =conn.cursor()

        cur.execute(f""" INSERT INTO χρηστης VALUES 
                ({id},'{διευθυσνη}',{ΑΦΜ},'{email}','{ημερομηνια}',{τηλ},{φωτογραφια});""")
        conn.commit()
    except :
        return -1
    return 0

def insert_aggelia(conn,id,εμφανισεις,ημερομηνια,ζητηση_πωληση,τιμη,τυποςοχηματος,περιγραφη,περιοχη,οχημα,συντακτης,ποσοχρεωσης,καταστασηχρεωσης,τροποςπληρωμης):
    try:
        cur =conn.cursor()

        cur.execute(f""" INSERT INTO αγγελία VALUES 
                ({id},{εμφανισεις},'{ημερομηνια}',{ζητηση_πωληση},{τιμη},'{τυποςοχηματος}','{περιγραφη}','{περιοχη}','{οχημα}',{συντακτης},{ποσοχρεωσης},'{καταστασηχρεωσης}','{τροποςπληρωμης}');""")
        conn.commit()
    except :
        return -1
    return 0

def insert_minima(conn,id,ημερομηνια,κατασταση,κειμενο,αφορα):
    try:
        cur =conn.cursor()

        cur.execute(f""" INSERT INTO μηνυμα VALUES 
                ({id},'{ημερομηνια}','{κατασταση}','{κειμενο}',{αφορα});""")
        conn.commit()
    except AttributeError as e:
        print(e)
        return -1
    return 0

def refresh(filename):
    os.remove(filename)
    conn =sqlite3.connect(filename)
    cur =conn.cursor()
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
	ονομασια string,
	γεωγραφικες συντεταγμενες string,
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

CREATE TABLE φωτογραφία (
	id integer PRIMARY KEY AUTOINCREMENT,
	blob file blob,
	url string
);

CREATE TABLE idiotis (
	id integer,
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
	ημερομηνια date,
	κατασταση string,
	κειμενο text,
	αφορα integer
);

CREATE TABLE ανηκει (
	id integer PRIMARY KEY AUTOINCREMENT,
	αγγελια id integer,
	φωτο id integer
);

CREATE TABLE περιεχει (
	id integer PRIMARY KEY AUTOINCREMENT,
	φωτο id integer,
	μηνυμα id integer
);

CREATE TABLE λαμβανει (
	id integer PRIMARY KEY AUTOINCREMENT,
	χρηστης id integer,
	μηνυμα id integer
);

CREATE TABLE αποστελει (
	id integer PRIMARY KEY AUTOINCREMENT,
	χρηστης id integer,
	μηνυμα id integer
);

    """
    temp=a.split(";")
    for i in temp: 
        cur.execute(i)
    conn.close()