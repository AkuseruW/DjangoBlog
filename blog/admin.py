from django.contrib import admin

# Register your models here.
from blog.models import PostCategory, Post

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

