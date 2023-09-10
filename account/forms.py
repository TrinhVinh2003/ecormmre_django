from django import forms
from .models import InforAccount

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = InforAccount
        fields = ['name','company','locality','city','mobile']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'})



        }