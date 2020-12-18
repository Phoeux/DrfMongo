from django.contrib import admin
from rest_framework.authtoken.admin import User

from .models import AuthorField, Book, CommentField, BookThroughFields, GenreField


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Book, BookAdmin)
admin.site.register(BookThroughFields, BookAdmin)
admin.site.register([AuthorField, CommentField, GenreField])