from django.db import models
# Create your models here.

class Category(models.Model):
    '''
    mynovel分类表：小说类型分类如玄幻，言情...
    '''
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL,'正常'),
        (STATUS_DELETE,'删除'),
    )

    name = models.CharField(max_length = 50,verbose_name="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    is_nav = models.BooleanField(default=False,verbose_name="是否导航")

    # 将分类信息展示在通用模板上，通过是否is_nav字段来过滤;确认是否导航,展示效果顶层分类为True，底层分类为False
    @classmethod
    def get_navs(cls):
        categories = cls.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)
        return {
            'navs':nav_categories,
            'categories':normal_categories,
        }


    # 重构book_list视图，作用：book_list中处理数据逻辑过于复杂，通过函数调用方法，对处理逻辑进行整理；此处为在category出找寻分类，在book处处理找寻图书
    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category = None
            books = []
        else:
            # 按照当前分类查找图书，由于Book中的category外键使其等于方法中当前查询到的的category并作为条件检索图书
            books = Book.objects.filter(category=category)
        return books,category

    # 返回类名称
    def __str__(self):
        return self.name

    class Meta:
        # 分类表
        verbose_name = verbose_name_plural = '小说分类'

class Book(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(max_length=255,verbose_name="书名")
    author = models.CharField(max_length=20,verbose_name="作者")
    description = models.CharField(max_length=1024,blank=True,verbose_name="简介")
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name="状态")
    update_time = models.DateTimeField(auto_now_add=True,verbose_name="再次更新时间")
    category = models.ForeignKey(Category,verbose_name="分类")

    # 添加字段pv最新书籍，uv最热书籍分别来统计文章的访问数量
    pv = models.PositiveIntegerField(default=1)
    uv = models.PositiveIntegerField(default=1)

    # 重构book_list视图，作用：book_list中处理数据逻辑过于复杂，通过函数调用方法，对处理逻辑进行整理；
    @staticmethod
    def get_by_book(book_id):
        try:
            books = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            books = []
        return books
    @classmethod
    def latest_books(cls):
        queryset = cls.objects.filter(status=cls.STATUS_NORMAL)
        return queryset

    # 将最新书籍和最热书籍加入Book方法中
    @classmethod
    def hot_books(cls):
        # 返回Book查询，以默认为过滤以字段pv过滤
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv')

    # 返回类名称
    def __str__(self):
        return self.title

    class Meta:
        # 图书表
        verbose_name = verbose_name_plural = '图书列表'
