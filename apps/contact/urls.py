from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('submit/', views.ContactSubmitView.as_view(), name='submit_contact'),
]