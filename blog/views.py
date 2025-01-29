from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.core.paginator import Paginator
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def blog_view(request,cat_name=None, author_username=None,tag_name=None):
    posts = Post.objects.filter(status = 1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if tag_name:
        posts = posts.filter(tags__name=tag_name)
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)
    
def blog_single(request, pk):
    posts = get_object_or_404(Post, pk=pk) 
    
    prev_post = Post.objects.filter(created_date__lt=posts.created_date).order_by('-created_date').first()
    next_post = Post.objects.filter(created_date__gt=posts.created_date).order_by('created_date').first()
    comments = Comment.objects.filter(post=posts.id, approved = True).order_by('-created_date')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Sent The Message!')
        else:
            messages.error(request, 'Please correct the errors below.')
    form = CommentForm()
    context = {'posts': posts, "prev_post":prev_post, "next_post":next_post, "comments": comments, "form": form}
    return render(request, "blog/blog-single.html", context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains= request.GET.get("s"))
    context  = {'posts': posts}
    return render(request,"blog/blog-home.html" ,context) 

from .forms import PostForm

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, "Post created successfully!")
            return redirect('blog:index_blog')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


def add_comment(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # ثبت کاربر
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form})
