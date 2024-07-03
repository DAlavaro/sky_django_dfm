from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from app.catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionListView, VersionCreateView, VersionUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),

    path('create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/<int:pk>/update/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('versions/<int:pk>/versions/', VersionListView.as_view(), name='product_versions'),
    path('versions/create/', VersionCreateView.as_view(), name='version_create'),
    path('product/<int:product_pk>/versions/<int:version_pk>/update/', VersionUpdateView.as_view(), name='version_update'),
]
