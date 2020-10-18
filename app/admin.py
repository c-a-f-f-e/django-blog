from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category) # 追加
# Register your models here.
