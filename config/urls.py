from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.catalog.urls'), name='catalog'),
    path('blog/', include('app.blog.urls'), name='blog'),
    path('users/', include('app.users.urls'), name='users'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

