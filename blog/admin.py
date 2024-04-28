from django.contrib import admin
from blog.models import Tag, Post

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'published_at')
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)