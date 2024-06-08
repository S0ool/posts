from django.contrib import admin

from app.models import Comment, Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", 'category')
    search_fields = 'title',
    list_filter = 'title',


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author",)
    search_fields = 'author',
    list_filter = 'author',


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = 'name',
    list_filter = 'name',


# Register your models here.
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
