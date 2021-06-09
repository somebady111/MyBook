from django.shortcuts import render
from .models import Chapter
from novel.models import Book,Category
from comment.models import Comment
# Create your views here.

from django.views.generic import DetailView

# 图书信息部分,通用部分
class BookDetailCommentView(DetailView):

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        books = self.kwargs.get('book_id')
        context.update({
            'books':books,
        })

    def get_queryset(self):
        queryset = Book.latest_books()
        return queryset

# 章节内容部分
class BookDetailView(BookDetailCommentView,DetailView):
    models = Chapter
    queryset = Chapter.latest_chapter()
    print(queryset)
    template_name = 'books/detail.html'
