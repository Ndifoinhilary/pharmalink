from . models import Contact, Pharmacy,Drug,Event, Staff
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        exclude = ['id','created_date','']
        fields = '__all__'
    
    


class DrugForm(forms.ModelForm):
    
    class Meta:
        model = Drug
        exclude = ['id','pharmacy']
        fields = "__all__"


class UserForm(UserCreationForm):
    # pharmacy = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email']

    def get_pharmacy(self):
        pharmacy = self.cleaned_data.get('pharmacy')
        if Pharmacy.objects.filter(pk=pharmacy).exists():
            return pharmacy
        
        raise forms.ValidationError("Pharmacy does not exist")

class StaffForm(forms.ModelForm):
    
    class Meta:
        model = Staff
        fields = ("pharmacy",)


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"
