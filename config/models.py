from django.db import models
from novel.models import Book
# Create your models here.

class Link(models.Model):

    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(max_length=50,verbose_name="友链标题")
    href = models.URLField(verbose_name="友链链接")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    weight = models.PositiveIntegerField(default=1,choices=zip(range(1,6),range(1,6)),verbose_name="权重",help_text="权重高展示顺序靠前")

    # 返回类名称
    def __str__(self):
        return self.title

    class Meta:
        # 链接表
        verbose_name = verbose_name_plural = '友链'

class SiderBar(models.Model):
    # 魔术数字：模板数据获取后得到的不是想看到的文字而是规定的数字,现更改如下
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏'),
    )

    DISPLAY_NEWBOOK = 1
    DISPLAY_HOTBOOK = 2
    DISPLAY_RECOMMENTBOOK = 3
    DISPLAY_HTML = 4
    SIDE_TYPE = (
        (DISPLAY_NEWBOOK,'最新图书'),
        (DISPLAY_HOTBOOK,'最热图书'),
        (DISPLAY_RECOMMENTBOOK,'推荐图书'),
        (DISPLAY_HTML,'HTML'),
    )

    title = models.CharField(max_length=20,verbose_name="侧边栏标题",blank=True)
    type = models.PositiveIntegerField(default=1,choices=SIDE_TYPE,verbose_name="类型")
    status = models.PositiveIntegerField(default=STATUS_SHOW,choices=STATUS_ITEMS,verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    book = models.ForeignKey(Book,verbose_name="书名")

    # 配置侧边栏，使得在book_list和book_detail中可以看到展示的侧边栏
    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=SiderBar.STATUS_SHOW)

    # 返回类名称
    def __str__(self):
        return self.title

    class Meta:
        # 侧边栏
        verbose_name = verbose_name_plural = '侧边栏'