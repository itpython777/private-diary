from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include
from .admin import mypage_site

from . import settings

admin.site.site_title = 'Administrator'
admin.site.site_header = 'Administrator'
admin.site.index_title = 'Menu'
admin.site.disable_action('delete_selected')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),
    path('myprofile/', include('myprofile.urls')),
    path('accounts/', include('allauth.urls')),
    
    path('mypage/', mypage_site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 開発サーバーでメディアを配信できるようにする設定
