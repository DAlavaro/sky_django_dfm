from django.urls import path
from app.blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<str:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<str:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]