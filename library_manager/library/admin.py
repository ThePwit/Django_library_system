
from django.contrib import admin
#from .models import LibraryBooks, LibraryLoaned, LibraryMembers, LibraryStaff, LibraryAuthor, LibraryGenre, LibraryBranch, LibraryPublisher
from .models import *
import string

"""
    Setup of the Admin Panel,
    Each Panel has it's own class to make them
    more managable, they also have filters selected for there individual contents
        
"""

class FirstLetterLastNameFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'First Letter'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'letter'
    letters = list(string.ascii_uppercase)

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        lookups = []
        for letter in self.letters:
            count = qs.filter(last_name__istartswith=letter).count()
            if count:
                lookups.append((letter, '{} ({})'.format(letter, count)))
        return lookups

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        filter_val = self.value()
        if filter_val in self.letters:
            return queryset.filter(last_name__istartswith=self.value())


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'authorid')
    list_display_links = ('title', 'isbn')
    list_filter = ('authorid', 'genreid', 'publisherid')
    ordering = ('authorid', )
    
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'job')
    list_filter = (FirstLetterLastNameFilter, )
    
class MembersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    list_filter = (FirstLetterLastNameFilter, )
    
class LoanedAdmin(admin.ModelAdmin):
    list_display = ('memberid', 'bookid', 'loandate', 'returndate')
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    ordering = ('last_name', )
    list_filter = (FirstLetterLastNameFilter, )
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre', )
    
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch','address' )
    
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', )

# Register your models here.
admin.site.site_header = 'Library Management System Admin Panel'
admin.site.register(LibraryBooks, BookAdmin)
admin.site.register(LibraryLoaned, LoanedAdmin)
admin.site.register(LibraryMembers, MembersAdmin)
admin.site.register(LibraryStaff, StaffAdmin)
admin.site.register(LibraryAuthor, AuthorAdmin)
admin.site.register(LibraryGenre, GenreAdmin)
admin.site.register(LibraryBranch, BranchAdmin)
admin.site.register(LibraryPublisher, PublisherAdmin)

