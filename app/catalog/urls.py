from django.urls import path
from app.catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, VersionListView, VersionCreateView, VersionUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),

    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('versions/<int:pk>/versions/', VersionListView.as_view(), name='product_versions'),
    path('versions/create/', VersionCreateView.as_view(), name='version_create'),
    path('product/<int:product_pk>/versions/<int:version_pk>/update/', VersionUpdateView.as_view(), name='version_update'),
]
