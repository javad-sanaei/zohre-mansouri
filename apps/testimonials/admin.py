from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_title', 'rating', 'is_active', 'sort_order', 'created_at')
    list_filter = ('is_active', 'rating')
    search_fields = ('student_name', 'comment')
    list_editable = ('is_active', 'sort_order')
    
    fieldsets = (
        ('اطلاعات دانشجو', {
            'fields': ('student_name', 'student_title', 'avatar_initial')
        }),
        ('نظر', {
            'fields': ('comment', 'rating')
        }),
        ('تنظیمات نمایش', {
            'fields': ('is_active', 'sort_order'),
            'description': 'ترتیب نمایش: عدد کمتر = اول نمایش داده شود'
        }),
    )