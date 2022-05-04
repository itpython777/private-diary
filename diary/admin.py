from django.contrib import admin
from .models import Diary, Category, Tag

class CategoryAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title')

    class Media:
        js = ('post.js',)

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Diary)

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import AdminSite

class DiaryAdminSite(AdminSite):
    site_header = 'マイページ'
    site_title = 'マイページ'
    index_title = 'ホーム'
    site_url = None
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


mypage_site = DiaryAdminSite(name="mypage")

mypage_site.register(Diary)
mypage_site.register(Tag)
mypage_site.register(Category)