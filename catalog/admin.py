from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language


# Inline class to display BookInstances in the Book detail view
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0  # No extra empty forms by default


# Define the admin class for Author with inlines for Books
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0  # No extra empty forms by default


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]  # Display related books inline in the Author detail view


# Register the Admin class for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]  # Display BookInstances inline in the Book detail view


# Register the Admin class for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')  # Updated display fields
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


# Register Genre and Language
admin.site.register(Genre)
admin.site.register(Language)
