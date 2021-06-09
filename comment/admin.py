from django.contrib import admin
from .models import Comment
from MyBook.custom_site import custom_site
from MyBook.base_admin import BaseOwnerAdmin
# Register your models here.

@admin.register(Comment,site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    # 查看展示
    list_display = ('comment_book','comment_chapter','nickname','content','create_time','status')
    # 编辑展示
    list_filter = ('comment_book','comment_chapter','nickname','content')
