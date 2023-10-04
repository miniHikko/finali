from django.urls import path
from django.views.decorators.cache import cache_page

from .views import NoticeList, create_post, PostDetail, create_comit, Comituser, Comittoouser

urlpatterns = [
    path('', (NoticeList.as_view()), name='news'),
    path('create/', create_post.as_view(), name='news_create'),
    path('<int:pk>', PostDetail.as_view(), name="details"),
    path('comit/', create_comit.as_view(success_url="/noticeboard/"), name='comit'),
    path('urcomit/', Comituser.as_view(), name='urcomit'),
    path("comitto/", Comittoouser, name=('comitto')),
]
