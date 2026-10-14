from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import Post, Category, Tag


class PostListView(ListView):
    """لیست همه مقالات"""
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.filter(status='published')
        
        # جستجو
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(
                models.Q(title__icontains=search_query) |
                models.Q(content__icontains=search_query) |
                models.Q(category__name__icontains=search_query)
            )
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['popular_posts'] = Post.objects.filter(
            status='published'
        ).order_by('-views_count')[:5]
        context['tags'] = Tag.objects.all()
        return context


class PostDetailView(DetailView):
    """نمایش تک مقاله"""
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = get_object_or_404(Post, slug=self.kwargs['slug'], status='published')
        
        # افزایش بازدید
        post.increase_view(self.request)
        
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        
        # مقالات مرتبط
        context['related_posts'] = Post.objects.filter(
            category=post.category,
            status='published'
        ).exclude(id=post.id)[:3]
        
        # کامنت‌های تأیید شده
        context['comments'] = post.comments.filter(is_approved=True)
        
        # مقالات پرطرفدار
        context['popular_posts'] = Post.objects.filter(
            status='published'
        ).order_by('-views_count')[:5]
        
        return context


class PostByCategoryView(ListView):
    """مقالات بر اساس دسته‌بندی"""
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category, status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = self.category
        context['categories'] = Category.objects.all()
        return context


class PostByTagView(ListView):
    """مقالات بر اساس تگ"""
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tags=self.tag, status='published')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_tag'] = self.tag
        context['tags'] = Tag.objects.all()
        return context