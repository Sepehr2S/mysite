from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator

def blog_view(request,cat_name=None):
    posts = Post.objects.filter(status = 1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': page_obj}
    return render(request, "blog/blog-home.html", context)
    
def blog_single(request, pk):
    posts = get_object_or_404(Post, pk=pk) 
    
    prev_post = Post.objects.filter(created_date__lt=posts.created_date).order_by('-created_date').first()
    next_post = Post.objects.filter(created_date__gt=posts.created_date).order_by('created_date').first()
    
    context = {'posts': posts, "prev_post":prev_post, "next_post":next_post}
    return render(request, "blog/blog-single.html", context)

def test(request):
    posts = Post.objects.all()  #pk hamoon id e
    context = {'posts': posts}
    return render(request, "test.html", context)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {"posts":posts}
    return render(request, "blog/blog-home.html", context)