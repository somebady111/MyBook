from django.db import models
from novel.models import Book
# Create your models here.

class Chapter(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    book = models.ForeignKey(Book,verbose_name="目标图书")
    chapters = models.CharField(max_length=50,verbose_name="章节名称")
    content = models.TextField(verbose_name="正文",help_text="内容为markdown格式")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    update_time = models.DateTimeField(auto_now_add=True,verbose_name="更新时间")

    @classmethod
    def latest_chapter(cls):
        book_id = None
        books = Book.get_by_book(book_id)
        queryset = cls.objects.filter(books)
        return queryset

    # 返回类名称
    def __str__(self):
        return self.chapters

    class Meta:
        # 图书表
        verbose_name = verbose_name_plural = '章节内容'