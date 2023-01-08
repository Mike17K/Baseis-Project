from contextlib import nullcontext
from django import forms


class CreateNewUserIdiotis(forms.Form):

    firstname = forms.CharField(label="First name",max_length=200)
    lastname = forms.CharField(label="Last name",max_length=200)

    address = forms.CharField(label="address",max_length=200)
    AFM = forms.IntegerField(label="AFM")
    email = forms.EmailField(label="Email",max_length=200)
    phone = forms.IntegerField(label="phone number")
    #photo = forms.ModelChoiceField(label="photo number",queryset=Speed.objects.all())


class CreateNewUserCompany(forms.Form):

    company_name = forms.CharField(label="company name",max_length=200)
    site = forms.CharField(label="site",max_length=200)
    business_type = forms.CharField(label="business type",max_length=200)

    address = forms.CharField(label="address",max_length=200)
    AFM = forms.IntegerField(label="AFM")
    email = forms.EmailField(label="Email",max_length=200)
    phone = forms.IntegerField(label="phone number")
    #photo = forms.ModelChoiceField(label="photo number",queryset=Speed.objects.all())


class CreateNewAggelia(forms.Form):
    zitisi_polisi = forms.ChoiceField(choices =(('z','zitisi'),('p','polisi')))
    timi = forms.FloatField(label="Price")
    vehicle_type = forms.ChoiceField(choices =(("Car","Car"),("Motorcycle","Motorcycle"),("Truck","Truck"),("MiniVan","MiniVan"),("SemiTruck","SemiTruck")))
    titlos = forms.CharField(label="Title",max_length=600)
    description = forms.CharField(label="Description",max_length=600)
    location = forms.ChoiceField(choices =[]) # edw locations 
    vehicle = forms.ChoiceField(choices =[]) # edw oximata 
    writer = forms.ChoiceField(choices=[])
    payment_method = forms.ChoiceField(choices =(("Debit Card","Debit"),("Τραπεζική Κατάθεση","Τράπεζα"),("Credit Card","Credit"))) # edw user

    class Meta:
        fields = ['zitisi_polisi','timi','vehicle_type','titlos','description',
        'location','vehicle','writer','payment_method']

    def __init__(self,*args, **kwargs):  
        vals = [kwargs.pop('location_new_choices', None),
        kwargs.pop('vehicle_new_choices', None),
        kwargs.pop('writer_new_choices', None)
        ]      
        super().__init__(*args, **kwargs)
        self.fields['location'].choices = vals[0]
        self.fields['vehicle'].choices = vals[1]
        self.fields['writer'].choices = vals[2]

        



class CreateNewMessage(forms.Form):
    message = forms.CharField(label="Message",max_length=500)

    aggelia = forms.ChoiceField(choices =[])
    sender = forms.ChoiceField(choices =[])

    class Meta:
        fields = ['message','aggelia','sender']

    def __init__(self,*args, **kwargs):        
        vals = [kwargs.pop('aggelia_new_choices',None),
        kwargs.pop('sender_new_choices',None)
        ]
        super().__init__(*args, **kwargs)
        self.fields['aggelia'].choices = vals[0]
        self.fields['sender'].choices = vals[1]
        

class CreateNewQuery(forms.Form):
    my_query = forms.CharField(label="Query",max_length=500,required=False)

class UserLoginForm(forms.Form):
    AFM = forms.IntegerField(label="AFM")
