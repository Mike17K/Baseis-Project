from contextlib import nullcontext
from django import forms

GEEKS_CHOICES = (("1", "One"),("2", "Two"),("3", "Three"),("4", "Four"),("5", "Five"))
PAYMENT_CHOICES = (("Debit Card","Debit"),("Τραπεζική Κατάθεση","Τράπεζα"),("Credit Card","Credit"))
class CreateNewUser(forms.Form):

    name = forms.CharField(label="name",max_length=200)
    address = forms.CharField(label="address",max_length=200)
    AFM = forms.IntegerField(label="AFM")
    email = forms.EmailField(label="Email",max_length=200)
    phone = forms.IntegerField(label="phone number")
    #photo = forms.ModelChoiceField(label="photo number",queryset=Speed.objects.all())

    isCompany = forms.BooleanField(label="Is Company",required=False)

class CreateNewAggelia(forms.Form):
    zitisi_polisi = forms.ChoiceField(choices =(('z','zitisi'),('p','polisi')))
    timi = forms.FloatField(label="Price")
    vehicle_type = forms.CharField(label="Vehicle Type",required=False)
    description = forms.CharField(label="Description",max_length=600)

    location = forms.ChoiceField(choices =GEEKS_CHOICES) # edw locations 
    vehicle = forms.ChoiceField(choices =GEEKS_CHOICES) # edw oximata 
    writer = forms.ChoiceField(choices =GEEKS_CHOICES) # edw user

    payment_method = forms.ChoiceField(choices =PAYMENT_CHOICES) # edw user


class CreateNewMessage(forms.Form):
    message = forms.CharField(label="Message",max_length=500)

    aggelia = forms.ChoiceField(choices =GEEKS_CHOICES)


class CreateNewQuery(forms.Form):
    my_query = forms.CharField(label="Query",max_length=500)