from django.shortcuts import render, redirect, get_object_or_404

from app.models import Post, Category, Comment


def post_constructor(post, request):
    post.title = request.POST.get('title')
    post.description = request.POST.get('description')
    post.content = request.POST.get('content')
    category_id = request.POST.get('category_id') or ''
    if category_id == '':
        return redirect('index')
    post.category = Category.objects.get(id=category_id)
    post.save()


def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    ctx = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'app/index.html', context=ctx)


def add_post(request):
    if (request.method != 'POST'
            or request.POST.get('title') == ''
            or request.POST.get('content') == ''
            or request.POST.get('category_id') == ''):
        return redirect('index')
    post = Post()

    post_constructor(post, request)
    return redirect('index')


def category(request):
    ctx = {
        'categories': Category.objects.all()
    }
    return render(request, 'app/category_html.html', context=ctx)


def category_info(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    ctx = {
        'category': category,
        'posts': category.posts.all()
    }
    return render(request, 'app/category_info.html', context=ctx)


def edit_category(request, category_id):
    if (request.method != 'POST'
            or request.POST.get('category_name') == ''):
        return redirect('category_info', category_id=category_id)

    category = get_object_or_404(Category, id=category_id)
    category.name = request.POST.get('category_name')
    category.save()
    return redirect('category_info', category_id=category_id)


def category_delete(request, category_id):
    if request.method != 'POST':
        return redirect('category_info', category_id=category_id)
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('category_page')


def add_category(request):
    if (request.method != 'POST'
            or request.POST.get('name') == ''):
        return redirect('category_page')
    category = Category()
    category.name = request.POST.get('name')
    category.save()
    return redirect('category_page')


def edit_post(request, post_id):
    if (request.method != 'POST'
            or request.POST.get('title') == ''
            or request.POST.get('content') == ''
            or request.POST.get('category_id') == ''):
        return redirect('post_info', post_id=post_id)
    post = get_object_or_404(Post, id=post_id)
    post_constructor(post, request)
    return redirect('post_info', post_id=post_id)


def post_delete(request, post_id):
    if request.method != 'POST':
        return redirect('post_info', post_id=post_id)

    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('index')


def post_info(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    ctx = {
        'post': post,
        'comments': Comment.objects.filter(post=post),
        'categories': Category.objects.all()
    }
    return render(request, 'app/post_info.html', context=ctx)


def add_comment(request):
    if (request.method != 'POST'
            or request.POST.get('author') == ''
            or request.POST.get('comment') == ''):
        return redirect('post_info', post_id=request.POST.get('post_id'))
    comment = Comment()
    comment.author = request.POST.get('author')
    comment.text = request.POST.get('comment')
    comment.post = Post.objects.get(id=request.POST.get('post_id'))
    comment.save()
    return redirect('post_info', post_id=request.POST.get('post_id'))
