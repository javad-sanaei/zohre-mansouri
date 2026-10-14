from django.contrib import admin
from .models import SiteSetting


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('label', 'key', 'section', 'field_type', 'is_active')
    list_filter = ('section', 'field_type', 'is_active')
    search_fields = ('label', 'key')
    list_editable = ('is_active',)
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('section', 'label', 'key', 'field_type')
        }),
        ('مقدار', {
            'fields': ('value',),
            'description': 'مقدار تنظیم مورد نظر را وارد کنید'
        }),
        ('راهنما', {
            'fields': ('help_text',)
        }),
        ('وضعیت', {
            'fields': ('is_active',)
        }),
    )