from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment, Category, Location, GalleryPic
from django.core.paginator import Paginator
from blog.forms import CommentForm, PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required





def blog_view(request, cat_name=None, author_username=None, tag_name=None):
    posts = Post.objects.filter(status=1)
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment successfully saved!')
        else:
            messages.error(request, 'Invalid comment.')
    posts = get_object_or_404(Post, pk=pk)
    locations = list(posts.locations.values('name', 'latitude', 'longitude'))
    prev_post = Post.objects.filter(created_date__lt=posts.created_date).order_by('-created_date').first()
    next_post = Post.objects.filter(created_date__gt=posts.created_date).order_by('created_date').first()
    comments = Comment.objects.filter(post=posts.id, approved=True).order_by('-created_date')
    gallery = GalleryPic.objects.filter(post=posts.id)
    form = CommentForm()
    
    context = {
        'posts': posts,
        'prev_post': prev_post,
        'next_post': next_post,
        'comments': comments,
        'form': form,
        'locations': locations,
        'gallery': gallery,  
    }
    return render(request, "blog/blog-single.html", context)




def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get("s"))
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)



@login_required
def create_post(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        files = request.FILES.getlist('gallery')  # دریافت لیست فایل‌های آپلود شده
    
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()

            # ذخیره تصاویر گالری
            for file in files:
                GalleryPic.objects.create(post=post, image=file)


            # دریافت مقادیر لوکیشن‌ها از فرم
            location_names = request.POST.getlist('location_name[]')
            latitudes = request.POST.getlist('latitude[]')
            longitudes = request.POST.getlist('longitude[]')

            print("📍 لوکیشن‌های دریافت شده:")
            for name, lat, lon in zip(location_names, latitudes, longitudes):
                print(f"  - {name}: ({lat}, {lon})")

            # ذخیره مکان‌ها و اتصال به پست
            for name, lat, lon in zip(location_names, latitudes, longitudes):
                try:
                    lat, lon = float(lat), float(lon)  # تبدیل به عدد برای جلوگیری از خطای متنی
                    location = Location.objects.create(name=name, latitude=lat, longitude=lon)
                    post.locations.add(location)
                except ValueError:
                    print(f"⚠️ مقدار نامعتبر دریافت شد: {lat}, {lon}")

            
            return redirect('blog:index_blog')
    else:
        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form, 'categories': categories})






def post_map(request, pk):
    post = get_object_or_404(Post, pk=pk)
    locations = list(post.locations.values('name', 'latitude', 'longitude'))

    context = {
        'post': post,
        'locations': locations,
    }
    return render(request, "blog/map.html", context)