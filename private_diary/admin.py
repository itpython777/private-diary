from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin import AdminSite

class BlogAdminSite(AdminSite):
    site_header = 'マイページ'
    site_title = 'マイページ'
    index_title = 'ホーム'
    site_url = None
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


mypage_site = BlogAdminSite(name="mypage")
