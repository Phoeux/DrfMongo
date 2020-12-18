from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from managebook.models import Book
from managebook.serializers import BookSerializer, BookFieldSerializer


class BookList(ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.all()


class BookFieldList(ListAPIView):
    serializer_class = BookFieldSerializer

    def get_queryset(self):
        return Book.objects.all()