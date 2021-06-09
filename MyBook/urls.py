"""MyBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .custom_site import custom_site

from novel.views import book_detail,book_list

# 类视图重构引入指定模块
from novel.views import BookListView,SearchView
# from chapter.views import BookDetailView

urlpatterns = [
    # 解耦硬编码:将写死的数据定义重新定义使其更好维护
    url(r'^super_admin/', admin.site.urls,name='super-admin'),
    url(r'^admin/',custom_site.urls,name='admin'),

    # url(r'^$',book_list),
    url(r'^$',BookListView.as_view()),
    url(r'^book/(?P<book_id>\d+).html$',book_detail,name='book-detail'),
    # url(r'^book/(?P<pk>\d+).html$',BookDetailView.as_view(),name='book-detail'),
    url(r'^category/(?P<category_id>\d+).html$',book_list,name='category-list'),
    url(r'^search/$',SearchView.as_view(),name='search')
]
