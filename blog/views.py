from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator

def blog_view(request,cat_name=None, author_username=None):
    posts = Post.objects.filter(status = 1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {'posts': posts}
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

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains= request.GET.get("s"))
    context  = {'posts': posts}
    return render(request,"blog/blog-home.html" ,context) 