from django.contrib import admin
from .models import Review, Post, Replie

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rate', 'comment', 'created_at']
    readonly_fields = ['created_at']

    list_filter = ['product']
    search_fields = ['product']
    filter_horizontal = ()

admin.site.register(Review, ReviewsAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['user1', 'post_id', 'post_content', 'timestamp']

    list_filter = ['user1']
    search_fields = ['user1', 'timestamp']
    filter_horizontal = ()

admin.site.register(Post, PostAdmin)


class RepliesAdmin(admin.ModelAdmin):
    list_display = ['user', 'reply_id', 'reply_content', 'post', 'timestamp']

    list_filter = ['user']
    search_fields = ['user1', 'timestamp']
    filter_horizontal = ()

admin.site.register(Replie, RepliesAdmin)
