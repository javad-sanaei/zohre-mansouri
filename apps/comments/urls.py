from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('submit/', views.CommentSubmitView.as_view(), name='submit_comment'),
]