from django.db import models


class SiteSetting(models.Model):
    """تنظیمات قابل تغییر سایت توسط مشاور"""
    
    FIELD_TYPE_CHOICES = (
        ('text', 'متن کوتاه'),
        ('textarea', 'متن بلند'),
        ('number', 'عدد'),
        ('image', 'تصویر'),
        ('video', 'ویدیو'),
        ('url', 'لینک'),
    )
    
    SECTION_CHOICES = (
        ('general', 'عمومی'),
        ('hero', 'بخش خانه'),
        ('about', 'درباره من'),
        ('achievements', 'افتخارات'),
        ('contact', 'تماس'),
        ('social', 'شبکه‌های اجتماعی'),
        ('seo', 'سئو'),
    )
    
    key = models.CharField(max_length=100, unique=True, verbose_name='کلید')
    value = models.TextField(verbose_name='مقدار')
    field_type = models.CharField(max_length=20, choices=FIELD_TYPE_CHOICES, default='text', verbose_name='نوع فیلد')
    section = models.CharField(max_length=20, choices=SECTION_CHOICES, default='general', verbose_name='بخش')
    label = models.CharField(max_length=200, verbose_name='برچسب فارسی')
    help_text = models.CharField(max_length=300, blank=True, verbose_name='راهنما')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'
        ordering = ['section', 'id']
    
    def __str__(self):
        return f'{self.label} ({self.key})'
    
    @classmethod
    def get_setting(cls, key, default=''):
        """دریافت یک تنظیم خاص"""
        try:
            return cls.objects.get(key=key, is_active=True).value
        except cls.DoesNotExist:
            return default
    
    @classmethod
    def get_all_settings(cls):
        """دریافت همه تنظیمات به صورت دیکشنری"""
        settings = {}
        for s in cls.objects.filter(is_active=True):
            settings[s.key] = s.value
        return settings