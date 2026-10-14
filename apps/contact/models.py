from django.db import models


class ContactRequest(models.Model):
    """مدل درخواست‌های مشاوره"""
    
    SERVICE_CHOICES = (
        ('کنکور', 'مشاوره کنکور'),
        ('انتخاب رشته', 'انتخاب رشته'),
        ('مدیریت استرس', 'مدیریت استرس'),
        ('تحصیل در خارج', 'تحصیل در خارج'),
        ('سایر', 'سایر'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'در انتظار'),
        ('contacted', 'تماس گرفته شده'),
        ('done', 'انجام شده'),
        ('rejected', 'رد شده'),
    )
    
    name = models.CharField(max_length=200, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=20, verbose_name='شماره تماس')
    email = models.EmailField(blank=True, verbose_name='ایمیل')
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES, verbose_name='نوع مشاوره')
    message = models.TextField(blank=True, verbose_name='پیام')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name='وضعیت')
    admin_notes = models.TextField(blank=True, verbose_name='یادداشت ادمین')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    
    class Meta:
        verbose_name = 'درخواست مشاوره'
        verbose_name_plural = 'درخواست‌های مشاوره'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.name} - {self.service_type}'