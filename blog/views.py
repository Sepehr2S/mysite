from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)
    
def blog_single(request, pid):
    posts = get_object_or_404(Post, pk=pid)
    context = {'posts': posts}
    return render(request, "blog/blog-single.html", context)

def test(request, pid):
    posts = get_object_or_404(Post, pk=pid)   #pk hamoon id e
    context = {'posts': posts}
    return render(request, "test.html", context)
