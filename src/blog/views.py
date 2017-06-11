from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Author, Blog
from .forms import PostCommentForm

# Create your views here.


def post_list(request):
    blog_list_query = Blog.objects.all()
    paginator = Paginator(blog_list_query, 4)
    page = request.GET.get('page')
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        blog_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        blog_list = paginator.page(paginator.num_pages)
    category_list = Category.objects.all()
    author_list = Author.objects.all()
    context = {
        "blog_list": blog_list,
        "category_list": category_list,
        "author_list": author_list
    }
    return render(request, 'post_list.html', context)


def view_post(request, slug):
    category_list = Category.objects.all()
    instance = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.given_by = request.user
            form_instance.save()
            instance.comments.add(form_instance)
            instance.save()
            return redirect(request.META['HTTP_REFERER'], '/')
    else:
        form = PostCommentForm()
    context = {
        'category_list': category_list,
        'instance': instance,
        'form': form
    }
    return render(request, 'view_post.html', context)


def view_category(request, slug):
    category_list = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    posts = Blog.objects.filter(category=category)
    context = {
        'category_list': category_list,
        'category': category,
        'posts': posts,
    }
    return render(request, 'view_category.html', context)


def view_author(request, slug):
    category_list = Category.objects.all()
    author = get_object_or_404(Author, slug=slug)
    posts = Blog.objects.filter(author=author)
    context = {
        'category_list': category_list,
        'author': author,
        'posts': posts
    }
    return render(request, 'view_author.html', context)
