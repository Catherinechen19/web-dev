from django.contrib import admin
from .models import Transaction


# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'item', 'status', 'purchase_date']
    # readonly_fields = [' date_updated']

    list_filter = ['status']
    search_fields = ['user']
    filter_horizontal = ()


admin.site.register(Transaction, TransactionAdmin)