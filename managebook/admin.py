from django.contrib import admin
from rest_framework.authtoken.admin import User

from .models import Author, Book, Comment

admin.site.register([Book])