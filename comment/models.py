from django.db import models
from novel.models import Book
from chapter.models import Chapter
# Create your models here.

class Comment(models.Model):

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    comment_book = models.ForeignKey(Book,verbose_name="评论小说")
    comment_chapter = models.ForeignKey(Chapter,verbose_name="评论章节")
    content = models.CharField(max_length=2000,verbose_name="评论内容")
    nickname = models.CharField(max_length=50,verbose_name="昵称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    # 重构book_detail,将评论的查找写入models
    @staticmethod
    def get_by_comment(books):
        try:
            comments = Comment.objects.filter(comment_book=books)
        except Comment.DoesNotExist:
            comments = None
        return comments

    # 返回类名称
    def __str__(self):
        return self.nickname

    class Meta:
        # 评论表
        verbose_name = verbose_name_plural = '评论'
