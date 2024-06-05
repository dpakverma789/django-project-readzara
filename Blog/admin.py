from django.contrib import admin
from .models import Post


# Register your models here.
class PostDetails(admin.ModelAdmin):
    list_display = ('post_title', 'post_author', 'post_date', 'post_clicks')


admin.site.register(Post, PostDetails)
