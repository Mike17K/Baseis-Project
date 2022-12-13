from django import forms

GEEKS_CHOICES = (("1", "One"),("2", "Two"),("3", "Three"),("4", "Four"),("5", "Five"))

class CreateNewUser(forms.Form):

    name = forms.CharField(label="name",max_length=200)
    address = forms.CharField(label="address",max_length=200)
    AFM = forms.IntegerField(label="AFM")
    email = forms.EmailField(label="Email",max_length=200)
    phone = forms.IntegerField(label="phone number")
    #photo = forms.ModelChoiceField(label="photo number",queryset=Speed.objects.all())

    isCompany = forms.BooleanField(label="Is Company",required=False)

class CreateNewMessage(forms.Form):
    text = forms.CharField(label="Message",max_length=500)

    aggelia = forms.ChoiceField(choices =GEEKS_CHOICES)

class CreateNewAggelia(forms.Form):
    pass
    
class CreateNewQuery(forms.Form):
    text = forms.CharField(label="Query",max_length=500)