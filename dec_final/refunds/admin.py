from django.contrib import admin
from .models import Refund

class RefundsAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'description', 'status', 'image']

    list_filter = ['user']
    search_fields = ['user']
    filter_horizontal = ()

admin.site.register(Refund, RefundsAdmin)