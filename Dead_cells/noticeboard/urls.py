from django.urls import path
from django.views.decorators.cache import cache_page

from .views import NoticeList, create_post, PostDetail

urlpatterns = [
    path('', (NoticeList.as_view()), name='news'),
    path('create/', create_post.as_view(), name='news_create'),
    path('<int:pk>', PostDetail.as_view(), name="details"),
    ]