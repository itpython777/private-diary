from django.urls import path
from .admin import mypage_site
from . import views


app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('top/', views.TopView.as_view(), name="top"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
    
    path('mypage/', mypage_site.urls),
]