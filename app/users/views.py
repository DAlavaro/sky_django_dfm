from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import PasswordResetView as BasePasswordResetView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, View

from app.users.forms import UserForm, LoginForm
from app.users.models import Users, EmailVerificationToken


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    form_class = LoginForm


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = Users
    form_class = UserForm
    success_url = reverse_lazy('users:register_done')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        new_object = form.save()
        token = EmailVerificationToken.objects.create(user=new_object)
        verification_url = self.request.build_absolute_uri(reverse(viewname='users:verify_email', kwargs={'token': token.token}))
        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Для подтверждения регистрации перейдите по ссылке: {verification_url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_object.email],
        )
        return super().form_valid(form)


def register_done(request):
    return render(request, 'users/register_done.html')


class EmailVerifyView(View):
    def get(self, request, token, *args, **kwargs):
        try:
            verification_token = EmailVerificationToken.objects.get(token=token)
            user = verification_token.user
            user.is_active = True
            user.save()
            verification_token.delete()
            return redirect('users:login')
        except EmailVerificationToken.DoesNotExist:
            return HttpResponse(content='Неверный или истекший токен верификации', status=400)


class MyPasswordResetView(BasePasswordResetView):
    template_name = 'users/password_reset_form.html'


def password_reset_done(request):
    return render(request, 'users/password_reset_done.html')


@require_http_methods(["POST"])
def generate_new_password(request):
    email = request.POST.get('email')
    if email:
        try:
            user = Users.objects.get(email=email)
            new_password = Users.objects.make_random_password()

            send_mail(
                subject='Восстановление пароля',
                message='Ваш новый пароль: ' + new_password,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
            )

            user.set_password(new_password)
            user.save()
            return redirect(reverse('users:password_reset_done'))

        except Users.DoesNotExist:
            return redirect(reverse('users:password_reset_done'))

    return redirect(reverse('users:password_reset_done'))



