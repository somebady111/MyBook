from django.contrib import admin
from .models import Link,SiderBar
from MyBook.custom_site import custom_site
from MyBook.base_admin import BaseOwnerAdmin
# Register your models here.

@admin.register(Link,site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title','href','status','create_time')
    fields = ('title','href','status','weight')

@admin.register(SiderBar,site=custom_site)
class SiderBarAdmin(BaseOwnerAdmin):
    list_display = ('title','type','create_time','status','book')
    fields = ('title','type','book','status')