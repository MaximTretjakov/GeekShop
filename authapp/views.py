from django.views.generic import FormView, View
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.urls import reverse


class LoginPageView(FormView):
    def post(self, request, *args, **kwargs):
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('mainapp:home'))
            else:
                return HttpResponse('Invalid login')
        else:
            return HttpResponseRedirect(reverse('authapp:login'))

    def get(self, request, *args, **kwargs):
        title = 'вход'
        login_form = ShopUserLoginForm(data=request.POST or None)
        content = {'title': title, 'login_form': login_form}
        return render(request, 'authapp/login.html', content)


class LogoutPageView(View):
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('mainapp:home'))


class RegisterPageView(FormView):
    def post(self, request, *args, **kwargs):
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
        else:
            return render(request, 'authapp/register.html', {'register_form': register_form})

    def get(self, request, *args, **kwargs):
        title = 'регистрация'
        register_form = ShopUserRegisterForm()
        content = {'title': title, 'register_form': register_form}
        return render(request, 'authapp/register.html', content)


class EditPageView(FormView):
    def post(self, request, *args, **kwargs):
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('authapp:edit'))
        else:
            return render(request, 'authapp/edit.html', {'edit_form': edit_form})

    def get(self, request, *args, **kwargs):
        title = 'редактирование'
        edit_form = ShopUserEditForm(instance=request.user)
        content = {'title': title, 'edit_form': edit_form}
        return render(request, 'authapp/edit.html', content)
