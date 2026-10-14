from django.contrib import admin
from .models import Category, Tag, Post, PostView


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'post_type', 'status', 'views_count', 'published_at')
    list_filter = ('status', 'post_type', 'category', 'tags')
    search_fields = ('title', 'content', 'meta_keywords')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views_count', 'video_views_count', 'created_at', 'updated_at')
    filter_horizontal = ('tags',)
    date_hierarchy = 'published_at'
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'category', 'tags', 'post_type', 'status')
        }),
        ('محتوا', {
            'fields': ('content', 'excerpt', 'featured_image')
        }),
        ('ویدیو', {
            'fields': ('video_url', 'video_file'),
            'description': 'می‌توانید لینک ویدیو (آپارات/یوتیوب) یا فایل ویدیو را آپلود کنید'
        }),
        ('سئو (اختیاری)', {
            'fields': ('meta_description', 'meta_keywords'),
            'description': 'برای بهبود رتبه در گوگل پر کنید. اگر خالی بماند، از متن مقاله استفاده می‌شود.',
            'classes': ('collapse',)
        }),
        ('آمار', {
            'fields': ('views_count', 'video_views_count'),
        }),
        ('زمان‌بندی', {
            'fields': ('published_at', 'created_at', 'updated_at'),
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if obj.status == 'published' and not obj.published_at:
            from django.utils import timezone
            obj.published_at = timezone.now()
        super().save_model(request, obj, form, change)


@admin.register(PostView)
class PostViewAdmin(admin.ModelAdmin):
    list_display = ('post', 'ip_address', 'viewed_at')
    readonly_fields = ('post', 'ip_address', 'session_key', 'viewed_at')
    
    def has_add_permission(self, request):
        return False