from django.apps import AppConfig
#from django.core import signals
from django.db.models import signals
from django.core.mail import send_mail
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import LibraryBooks, LibraryMembers

@receiver(signals.post_save, sender=LibraryBooks)
def send_post_mail(sender, instance, created, **kwargs):
    book=LibraryBooks.objects.all().last()
    recipient_list = LibraryMembers.objects.exclude(email='').values_list('email', flat=True)
    print('signal send')
    subject = "A new book has been added"
    body = f'{book.title} has been added to our collection'
    send_mail(subject, body, 'sender@gmail.com', 
    recipient_list, fail_silently=False,)
    
@receiver(signals.post_delete, sender=User)
def delete_member(sender, instance, *args, **kwargs):
    member = LibraryMembers.objects.filter(userid=User.id)
    member.delete()