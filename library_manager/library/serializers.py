from .models import *
from rest_framework import serializers

#Query Sets ----> Dictionaries ----> JSON -=- Serialization
#JSON ----> Dictionaries ----> Query Sets -=- Deserialization


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryBooks
        fields = "__all__"
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryAuthor
        fields = "__all__"