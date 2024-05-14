from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category


NUM_POSTS_INDEX = 5


def some_posts(post_objects):
    """Посты из БД"""
    return post_objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    """Главная страница"""
    template = 'blog/index.html'
    post_list = some_posts(Post.objects)[:NUM_POSTS_INDEX]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Описание записи в блоге"""
    template = 'blog/detail.html'
    post = get_object_or_404(some_posts(Post.objects), pk=post_id)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Публикация категории"""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = some_posts(category.posts)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
