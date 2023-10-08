from django.urls import path
from .views import NoticeList, create_post, PostDetail, create_comit, Comituser, ComDelete

urlpatterns = [
    path('', (NoticeList.as_view()), name='news'),
    path('create/', create_post.as_view(), name='news_create'),
    path('<int:pk>', PostDetail.as_view(), name="details"),
    path('comit/', create_comit.as_view(success_url="/noticeboard/"), name='comit'),
    path('urcomit/', Comituser.as_view(), name='urcomit'),
    path('urcomit/<int:pk>/del', ComDelete.as_view(), name='delcom')

]
