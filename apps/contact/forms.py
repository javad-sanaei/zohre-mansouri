from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'phone', 'email', 'service_type', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'name': 'نام و نام خانوادگی',
            'phone': 'شماره تماس',
            'email': 'ایمیل',
            'service_type': 'نوع مشاوره',
            'message': 'پیام',
        }