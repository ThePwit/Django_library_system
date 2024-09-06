
from django import forms
from .models import LibraryBooks

class AddBook(forms.ModelForm):
    
    class Meta:       
        model = LibraryBooks
        fields = ('title', 'isbn', 'libraryid', 'publisherid', 'authorid', 'genreid')
        
        ''' widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'libraryid': forms.TextInput(attrs={'class': 'form-control'}),
            'publisherid': forms.TextInput(attrs={'class': 'form-control'}),
            'authorid': forms.TextInput(attrs={'class': 'form-control'}),
            'genreid': forms.TextInput(attrs={'class': 'form-control'}),
        }'''
    