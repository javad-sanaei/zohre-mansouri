from django.views.generic import ListView
from django.http import JsonResponse
from django.views import View
from .models import Testimonial


class TestimonialListView(View):
    """API دریافت نظرات فعال"""

    def get(self, request, *args, **kwargs):
        testimonials = Testimonial.objects.filter(
            is_active=True
        ).order_by('-created_at')

        data = [
            {
                'id': t.id,
                'student_name': t.student_name,
                'student_title': t.student_title,
                'avatar_initial': t.avatar_initial,
                'comment': t.comment,
                'rating': t.rating,
            }
            for t in testimonials
        ]

        return JsonResponse({'testimonials': data})