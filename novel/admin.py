from django.contrib import admin
from .models import Category,Book
from .adminforms import NovelAdmin
from MyBook.custom_site import custom_site
from django.utils.html import format_html
from django.urls import reverse
from django.contrib.admin.models import LogEntry
from MyBook.base_admin import BaseOwnerAdmin
from chapter.models import Chapter
# Register your models here.

@admin.register(Category,site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):

    # 添加book_count选项,为文章计数
    def Book_count(self, obj):
        return obj.book_set.count()
    Book_count.short_description = '该分类文章数量'

    # 查看时展示选项
    list_display = ('name','is_nav','status','create_time','Book_count')
    # 添加时展示选项
    fields = ('name','is_nav','status')

# 给文章增添章节内容添加选项
class ChapterInline(admin.TabularInline):
    fields = ('book','chapters','content')
    extra = 1
    model = Chapter

@admin.register(Book,site=custom_site)
class BookAdmin(BaseOwnerAdmin):

    # 引入自定义form
    form = NovelAdmin

    # 展示自定义字段
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            # 当前app下的model字段
            reverse('cus_admin:novel_book_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    # 查看时展示项
    list_display = (
        'title',
        'author',
        'description',
        'category',
        'update_time',
        'status',
        'operator',
    )
    list_display_links = []

    search_fields = ('title','category__name','author')

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                ('title','category','author'),
            ),
        }),
        ('简介',{
            'fields':(
                'description',
            ),
        }),
        ('简介',{
            'classes':('wide',),
            'fields':('status',),
        }),
    )

    # 添加增添章节选项
    inlines = [ChapterInline,]

    #控制多对多字段的展示效果
    # filter_vertical = ('author',)
    # filter_horizontal = ('title',)



    # 自定义静态资源
    # class Media:
    #     css = {
    #         'all':("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",)
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)

@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
