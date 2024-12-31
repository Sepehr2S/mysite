from django.contrib import admin
from blog.models import Post, Category, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    search_fields = ("title", "content",)
    list_display = ("title", "author", "status" , "created_date", "counted_views", )
    ordering= ("-created_date",)
    empty_value_display = ("-empty-",)
    list_filter = ("status","author")

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = ("-empty-",)
    list_display = ("name", "post", "approved", "created_date", )
    list_filter = ("post","approved")
    search_fields = ("name", "post")


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
