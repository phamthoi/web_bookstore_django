from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_id', 'title', 'author', 'date', 'book', 'cover_book']
    list_filter = ['book_id', 'title', 'author', 'date', 'book', 'cover_book']
    search_fields = ['title']
admin.site.register(Book, BookAdmin)