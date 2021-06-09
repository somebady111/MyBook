from django.contrib import admin
from MyBook.base_admin import BaseOwnerAdmin
from MyBook.custom_site import custom_site
from .models import Chapter
# Register your models here.


@admin.register(Chapter,site=custom_site)
class ChapterAdmin(BaseOwnerAdmin):

    list_display = (
        'book',
        'chapters',
        'content',
        'status',
        'update_time',
    )

    list_filter = (
        'book',
        'chapters',
        'content',
    )

