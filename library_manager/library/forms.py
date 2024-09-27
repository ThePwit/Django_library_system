
from django import forms
from .models import LibraryBooks, LibraryMembers
from django.contrib.auth.models import User

class AddBook(forms.ModelForm):
    
    class Meta:       
        model = LibraryBooks
        fields = ('title', 'isbn', 'libraryid', 'publisherid', 'authorid', 'genreid')
        
class UpdateUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')