from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField



class Category(models.Model):
    """دسته‌بندی مقالات"""
    name = models.CharField(max_length=200, verbose_name='نام دسته')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='اسلاگ')
    description = models.TextField(blank=True, verbose_name='توضیحات')
    icon = models.CharField(max_length=50, blank=True, verbose_name='آیکون (کلاس Font Awesome)')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی‌ها'
        ordering = ['id']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Tag(models.Model):
    """تگ‌های مقالات"""
    name = models.CharField(max_length=100, verbose_name='نام تگ')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='اسلاگ')
    
    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ‌ها'
        ordering = ['name']
    
    def __str__(self):
        return f'#{self.name}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Post(models.Model):
    """مدل مقاله"""
    
    STATUS_CHOICES = (
        ('draft', 'پیش‌نویس'),
        ('published', 'منتشر شده'),
    )
    
    POST_TYPE_CHOICES = (
        ('text', 'متنی'),
        ('video', 'ویدیویی'),
        ('image', 'تصویری'),
    )
    
    title = models.CharField(max_length=300, verbose_name='عنوان')
    slug = models.SlugField(unique=True, allow_unicode=True, verbose_name='اسلاگ')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts', verbose_name='دسته‌بندی')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts', verbose_name='تگ‌ها')
    
    # محتوا
    content = RichTextField(verbose_name='متن مقاله')
    excerpt = models.TextField(max_length=500, verbose_name='خلاصه مقاله')
    
    # تصویر شاخص
    featured_image = models.ImageField(upload_to='blog/posts/', verbose_name='تصویر شاخص')
    
    # ویدیو (اختیاری)
    video_url = models.URLField(blank=True, verbose_name='لینک ویدیو')
    video_file = models.FileField(upload_to='blog/videos/', blank=True, verbose_name='فایل ویدیو')
    
    # نوع پست
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='text', verbose_name='نوع پست')
    
    # وضعیت و آمار
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='وضعیت')
    views_count = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')
    video_views_count = models.PositiveIntegerField(default=0, verbose_name='بازدید ویدیو')
    
    # SEO
    meta_description = models.CharField(max_length=300, blank=True, verbose_name='توضیحات سئو')
    meta_keywords = models.CharField(max_length=300, blank=True, verbose_name='کلمات کلیدی')
    
    # زمان‌بندی
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='تاریخ انتشار')
    
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-published_at', '-created_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
    
    def increase_view(self, request):
        """افزایش بازدید"""
        from .models import PostView
        
        ip = request.META.get('REMOTE_ADDR')
        session_key = request.session.session_key
        
        # چک کن قبلاً این کاربر بازدید کرده یا نه
        if not PostView.objects.filter(post=self, ip_address=ip, session_key=session_key).exists():
            self.views_count += 1
            self.save(update_fields=['views_count'])
            
            PostView.objects.create(
                post=self,
                ip_address=ip,
                session_key=session_key
            )
    
    def increase_video_view(self, request):
        """افزایش بازدید ویدیو"""
        self.video_views_count += 1
        self.save(update_fields=['video_views_count'])


class PostView(models.Model):
    """ثبت بازدیدهای یکتا"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_views')
    ip_address = models.GenericIPAddressField()
    session_key = models.CharField(max_length=100)
    viewed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'بازدید'
        verbose_name_plural = 'بازدیدها'
        unique_together = ['post', 'ip_address', 'session_key']
    
    def __str__(self):
        return f'بازدید: {self.post.title}'