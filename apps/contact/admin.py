from django.contrib import admin
from .models import ContactRequest


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service_type', 'status', 'created_at')
    list_filter = ('status', 'service_type')
    search_fields = ('name', 'phone', 'email', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('status',)
    
    fieldsets = (
        ('اطلاعات تماس', {
            'fields': ('name', 'phone', 'email')
        }),
        ('درخواست', {
            'fields': ('service_type', 'message')
        }),
        ('مدیریت', {
            'fields': ('status', 'admin_notes'),
            'description': 'وضعیت درخواست را تغییر دهید و یادداشت خود را بنویسید'
        }),
        ('زمان', {
            'fields': ('created_at',),
        }),
    )