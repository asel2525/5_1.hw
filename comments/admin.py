from django.contrib import admin
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    field = ['question', 'contact']

admin.site.register(Comment, CommentAdmin)