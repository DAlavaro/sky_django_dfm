from django.urls import path

from app.catalog.views import home, contacts

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]