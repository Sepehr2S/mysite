from django import template
from blog.models import Post

register = template.Library()   

@register.simple_tag
def totalpost():
    posts = Post.objects.filter(status=1)
    total = 0
    for i in posts:
        if i:
            total += 1
    return total