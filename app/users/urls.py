from django.urls import path

from app.users.views import LoginView, LogoutView, RegisterView, EmailVerifyView, generate_new_password, \
    MyPasswordResetView, password_reset_done

app_name = 'users'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('verify_email/<uuid:token>/', EmailVerifyView.as_view(), name='verify_email'),

    path('password_reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('reset_password/', generate_new_password, name='reset_password'),  # URL для функции сброса пароля
    path('password_reset_done/', password_reset_done, name='password_reset_done'),

]
