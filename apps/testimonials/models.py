from django.db import models


class Testimonial(models.Model):
    """مدل نظرات دانشجوها"""
    
    student_name = models.CharField(max_length=200, verbose_name='نام دانشجو')
    student_title = models.CharField(max_length=300, verbose_name='عنوان (مثلاً: رتبه ۱۲ کنکور)')
    avatar_initial = models.CharField(max_length=10, verbose_name='حروف اول نام')
    comment = models.TextField(verbose_name='نظر')
    rating = models.PositiveSmallIntegerField(default=5, verbose_name='امتیاز (۱ تا ۵)')
    is_active = models.BooleanField(default=True, verbose_name='نمایش داده شود')
    sort_order = models.PositiveIntegerField(default=0, verbose_name='ترتیب نمایش')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات دانشجوها'
        ordering = ['sort_order', '-created_at']
    
    def __str__(self):
        return f'{self.student_name} - {self.student_title}'