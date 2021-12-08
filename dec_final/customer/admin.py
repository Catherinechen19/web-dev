from django.contrib import admin
from .models import Request


# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'description', 'category', 'image']

    list_filter = ['category', 'name', 'user']
    search_fields = ['category']
    filter_horizontal = ()


admin.site.register(Request, RequestAdmin)

