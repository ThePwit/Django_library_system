
from django import forms
from .models import LibraryBooks

class AddBook(forms.ModelForm):
    
    class Meta:       
        model = LibraryBooks
        fields = ('title', 'isbn', 'libraryid', 'publisherid', 'authorid', 'genreid')
        
