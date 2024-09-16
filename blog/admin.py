from django.contrib import admin
from blog.models import Post, Category

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    search_fields = ("title", "content",)
    list_display = ("title", "author", "status" , "created_date", "counted_views", )
    ordering= ("-created_date",)
    empty_value_display = ("-empty-",)
    list_filter = ("status","author")

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
