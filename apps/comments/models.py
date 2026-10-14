from django.db import models


class Comment(models.Model):
    """مدل کامنت‌های مقالات و نظرات"""

    name = models.CharField(max_length=200, verbose_name='نام')
    phone = models.CharField(max_length=20, verbose_name='شماره تماس')
    title = models.CharField(max_length=300, blank=True, verbose_name='عنوان')
    text = models.TextField(verbose_name='متن نظر')
    is_approved = models.BooleanField(default=False, verbose_name='تأیید شده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت‌ها'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.text[:50]}'