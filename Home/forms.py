from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields='__all__'
        '''
        label={
            'description':'Write your thoughts here :'
        }
        widgets={
            'title':    forms.TextInput(attrs={'class':'form-control my-5'})
        }
        '''
