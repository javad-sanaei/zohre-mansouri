from django.views.generic import FormView
from django.http import JsonResponse
from django.views import View
from .models import ContactRequest
from .forms import ContactForm


class ContactSubmitView(View):
    """ویو ارسال فرم تماس با AJAX"""

    def post(self, request, *args, **kwargs):
        # DEBUG - ببینیم چی داریم
        print("=" * 50)
        print("POST data:", request.POST)
        print("=" * 50)

        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()
            print(f"✅ ذخیره شد! ID: {contact.id}")
            return JsonResponse({
                'success': True,
                'message': 'پیام شما با موفقیت ارسال شد. به زودی با شما تماس می‌گیریم.'
            })

        print(f"❌ خطاهای فرم: {form.errors}")
        return JsonResponse({
            'success': False,
            'errors': form.errors
        }, status=400)