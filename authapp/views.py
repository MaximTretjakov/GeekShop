from django.views.generic import FormView, View
from django.db import transaction
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm, ShopUserProfileEditForm
from django.contrib import auth
from django.urls import reverse

from django.core.mail import send_mail
from django.conf import settings
from authapp.models import ShopUser


def send_verify_mail(user):
    verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} ' \
              f'перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


class VerifyPageView(View):
    def get(self, request, **kwargs):
        try:
            user = ShopUser.objects.get(email=kwargs['email'])
            if user.activation_key == kwargs['activation_key'] and not user.is_activation_key_expired():
                user.is_active = True
                user.save()
                auth.login(request, user)
                return render(request, 'authapp/verification.html')
            else:
                print(f'error activation user: {user}')
                return render(request, 'authapp/verification.html')
        except Exception as e:
            print(f'error activation user : {e.args}')
            return HttpResponseRedirect(reverse('home'))


class LoginPageView(FormView):
    def post(self, request, *args, **kwargs):
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('mainapp:home'))
            else:
                return HttpResponse('Invalid login')
        else:
            return HttpResponseRedirect(reverse('authapp:login'))

    def get(self, request, *args, **kwargs):
        title = 'вход'
        next_url = request.GET.get('next', '')
        login_form = ShopUserLoginForm(data=request.POST or None)
        content = {'title': title, 'login_form': login_form, 'next': next_url}
        return render(request, 'authapp/login.html', content)


class LogoutPageView(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('mainapp:home'))


class RegisterPageView(FormView):
    def post(self, request, *args, **kwargs):
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('authapp:login'))
        else:
            return render(request, 'authapp/register.html', {'register_form': register_form})

    def get(self, request, *args, **kwargs):
        title = 'регистрация'
        register_form = ShopUserRegisterForm()
        content = {'title': title, 'register_form': register_form}
        return render(request, 'authapp/register.html', content)


class EditPageView(FormView):
    @transaction.atomic
    def post(self, request, **kwargs):
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))

    def get(self, request, **kwargs):
        title = 'редактирование'
        edit_form = ShopUserEditForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)
        content = {
            'title': title,
            'edit_form': edit_form,
            'profile_form': profile_form
        }
        return render(request, 'authapp/edit.html', content)
