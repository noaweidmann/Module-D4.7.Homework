from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsCreate, ArticleCreate, NewsUpdate, ArticleUpdate, PostDelete

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', PostSearch.as_view(), name='search'),
    path('createnews/', NewsCreate.as_view(), name='news_create_edit'),
    path('createarticle/', ArticleCreate.as_view(), name='articles_create_edit'),
    path('<int:pk>/newsedit', NewsUpdate.as_view(), name='news_create_edit'),
    path('<int:pk>/articleedit', ArticleUpdate.as_view(), name='articles_create_edit'),
    path('<int:pk>/deletepost/', PostDelete.as_view(), name='delete_news_articles'),
]