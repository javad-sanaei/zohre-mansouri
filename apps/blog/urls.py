from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<path:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<path:slug>/', views.PostByCategoryView.as_view(), name='post_by_category'),
    path('tag/<path:slug>/', views.PostByTagView.as_view(), name='post_by_tag'),
]