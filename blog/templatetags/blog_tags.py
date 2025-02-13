from django import template
from blog.models import Post, Comment
from blog.models import Category
from django.utils import timezone
from datetime import timedelta
from persiantools.jdatetime import JalaliDateTime

register = template.Library()   

@register.simple_tag(name="totalposts")
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name="comments_count")   
def function(pid):
    post = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id, approved=True).count()
    
@register.simple_tag(name="posttitle")
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value, arg=20):
    return value[:arg] + "..."

@register.inclusion_tag("blog/blog-popularposts.html")
def latestposts():
    posts = Post.objects.filter(status=1).order_by("-published_date")[:3]
    return {"posts": posts}

@register.inclusion_tag("blog/blog-postcategories.html")
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories":cat_dict}

@register.filter
def persian_naturalday(value):
    now = timezone.now()
    delta = now - value

    if delta < timedelta(minutes=1):
        return "چند لحظه پیش"
    elif delta < timedelta(hours=1):
        return f"{int(delta.total_seconds() // 60)} دقیقه پیش"
    elif delta < timedelta(days=1):
        return f"{int(delta.total_seconds() // 3600)} ساعت پیش"
    elif delta < timedelta(days=2):
        return "دیروز"
    elif delta < timedelta(days=7):
        return f"{delta.days} روز پیش"
    else:
        jalali_date = JalaliDateTime.to_jalali(value)
        return jalali_date.strftime('%Y/%m/%d')