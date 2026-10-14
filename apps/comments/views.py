from django.http import JsonResponse
from django.views import View
from .models import Comment


class CommentSubmitView(View):
    """ویو ارسال کامنت با AJAX"""

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        title = request.POST.get('title', '')
        text = request.POST.get('comment', '')

        print(f"Received: name={name}, phone={phone}, title={title}, text={text}")

        if not all([name, phone, text]):
            return JsonResponse({
                'success': False,
                'message': 'لطفاً نام، شماره تماس و نظر خود را وارد کنید.'
            }, status=400)

        try:
            comment = Comment.objects.create(
                name=name,
                phone=phone,
                title=title,
                text=text,
                is_approved=False
            )

            return JsonResponse({
                'success': True,
                'message': 'نظر شما ثبت شد و پس از تأیید نمایش داده می‌شود.'
            })

        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({
                'success': False,
                'message': 'خطا در ثبت نظر. لطفاً دوباره تلاش کنید.'
            }, status=500)