from django.views.generic import TemplateView
from .models import SiteSetting
from apps.testimonials.models import Testimonial
from apps.comments.models import Comment  # ← اینو اضافه کن


class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # تنظیمات سایت
        settings = SiteSetting.get_all_settings()
        context['settings'] = settings

        # زبان‌ها
        languages_str = settings.get('languages', '')
        if '|' in languages_str:
            context['languages_list'] = [lang.strip() for lang in languages_str.split('|') if lang.strip()]
        else:
            context['languages_list'] = [lang.strip() for lang in languages_str.split(',') if lang.strip()]

        # ⭐ نظرات منتخب برای اسلایدر
        context['testimonials'] = Testimonial.objects.filter(is_active=True).order_by('sort_order', '-created_at')

        # 💬 کامنت‌های تأیید شده برای نمایش عمومی
        context['approved_comments'] = Comment.objects.filter(is_approved=True).order_by('-created_at')[:10]

        return context