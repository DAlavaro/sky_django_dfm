from django.urls import path
from django.views.decorators.cache import never_cache

from app.blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', never_cache(BlogCreateView.as_view()), name='blog_create'),
    path('<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<str:slug>/update/',  never_cache(BlogUpdateView.as_view()), name='blog_update'),
    path('<str:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]