from django.contrib import admin
from .models import Category, Author, Blog


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "updated"]
    prepopulated_fields = {"slug": ("title",)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "updated"]
    prepopulated_fields = {"slug": ("name",)}


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "created", "updated", "author", "category"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
