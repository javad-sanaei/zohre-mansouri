from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'title', 'is_approved', 'created_at')  # ← email رو با phone عوض کن
    list_filter = ('is_approved',)
    search_fields = ('name', 'phone', 'text', 'title')
    list_editable = ('is_approved',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ('اطلاعات', {
            'fields': ('name', 'phone', 'title')
        }),
        ('نظر', {
            'fields': ('text',)
        }),
        ('مدیریت', {
            'fields': ('is_approved',),
            'description': 'برای نمایش نظر در سایت، آن را تأیید کنید'
        }),
    )