from django.shortcuts import render
from django.http import HttpResponse

from .models import Category,Book
from config.models import SiderBar
from chapter.models import Chapter
from comment.models import Comment
# Create your views here.

# 类视图引入
from django.views.generic import DetailView,ListView

# 增加书列表类处理通用数据
class BookListCommonViewMixin(ListView):
    def get_context_data(self,**kwargs):
        category_id = None
        context = super().get_context_data(**kwargs)
        context.update({
            'siderbars': SiderBar.get_all(),
            'category': Category.get_by_category(category_id),
        })
        context.update(Category.get_navs())
        return context

# 类视图改写
class BookListView(BookListCommonViewMixin,ListView):
    queryset = Book.latest_books()
    paginate_by = 2
    # 具体展示那一项内容就要写当项查询,此处查询的是books所有书籍
    context_object_name = 'books'
    template_name = 'books/list.html'

# 搜索功能
from django.db.models import Q

class SearchView(BookListView):
    def get_book_data(self):
        context = super().get_context_data()
        context.update({
            'keyword':self.request.GET.get('keyword','')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title=keyword) | Q(author=keyword))

def book_detail(request,book_id=None,chaptes=None):
    try:
        books = Book.objects.get(id=book_id)
        # 以当前书籍id为条件进行章节搜索并展示
        chaptes = Chapter.objects.filter(book=books)
        # 评论查书
        comments = Comment.get_by_comment(books)
    except Book.DoesNotExist:
        books = None
        comments = None
    context = {
        'books':books,
        'chaptes':chaptes,
        'comments':comments,
    }
    context.update(Category.get_navs())
    return render(request,'books/detail.html',context=context)

def book_list(request,category_id=None,book_id=None):
    category = None
    if book_id:
        books = Book.get_by_book(book_id)
    elif category_id:
        books,category = Category.get_by_category(category_id)
    else:
        books = Book.latest_books()

    context = {
        'category':category,
        'books':books,
        'siderbars':SiderBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request,'books/list.html',context=context)

