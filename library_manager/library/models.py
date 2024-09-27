# importing required modules
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone

# ----------- Library Management System Models ------------

class LibraryAuthor(models.Model):
    """model for author table"""    
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        
    def __str__(self):
        return (self.first_name + " " + self.last_name)
        
class LibraryPublisher(models.Model):
    """model for publisher table"""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'publisher'
        verbose_name = 'Publisher'
        
    def __str__(self):
        return self.name
        
class LibraryGenre(models.Model):
    """model for genre table"""  
    id = models.BigAutoField(primary_key=True)
    genre = models.CharField(max_length=50)

    class Meta:
        db_table = 'genre'
        verbose_name = 'Genre'
        
    def __str__(self):
        return self.genre
        
class LibraryBranch(models.Model):
    """model for library table"""
    id = models.BigAutoField(primary_key=True)
    branch = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'library'
        verbose_name = 'Branch'
        
    def __str__(self):
        return self.branch
        
class LibraryMembers(models.Model):
    """model for members table"""
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    libraryid = models.ForeignKey(LibraryBranch, db_column='libraryid',  on_delete=models.CASCADE)
    userid = models.ForeignKey(User, db_column='userid',  on_delete=models.CASCADE)

    class Meta:
        db_table = 'members'
        verbose_name = 'Member'
        
    def __str__(self):
        return (self.first_name + " " + self.last_name)

class LibraryBooks(models.Model):
    """model for books table"""
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)
    authorid = models.ForeignKey(LibraryAuthor, db_column='authorid',  on_delete=models.CASCADE)
    genreid = models.ForeignKey(LibraryGenre, db_column='genreid', on_delete=models.CASCADE)
    libraryid = models.ForeignKey(LibraryBranch, db_column='libraryid', on_delete=models.CASCADE)
    publisherid = models.ForeignKey(LibraryPublisher, db_column='publisherid', on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'
        verbose_name = 'Book'
        
    def __str__(self):
        return self.title

class LibraryLoaned(models.Model):
    """model for loaned table"""
    id = models.BigAutoField(primary_key=True)
    loandate = models.DateField()
    returndate = models.DateField(blank=True, null=True)
    bookid = models.ForeignKey(LibraryBooks, db_column='bookid',  on_delete=models.CASCADE)
    memberid = models.ForeignKey(LibraryMembers, db_column='memberid',  on_delete=models.CASCADE)

    class Meta:
        db_table = 'loaned'
        verbose_name = 'Loan'
        
class LibraryStaff(models.Model):
    """model for staff table"""
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=25)
    libraryid = models.ForeignKey(LibraryBranch, db_column='libraryid',  on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'staff'
        verbose_name = 'Staff'
        
        
    def __str__(self):
        return (self.first_name + " " + self.last_name)
    