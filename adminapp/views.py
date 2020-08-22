from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import View, ListView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


# class UsersPageView(UserPassesTestMixin, View):
#     def test_func(self):
#         return self.request.user.is_superuser
#
#     def post(self, request):
#         pass
#
#     def get(self, request):
#         title = 'админка / пользователи'
#         users_list = ShopUser.objects.all()
#         content = {
#             'title': title,
#             'objects': users_list
#         }
#         return render(request, 'adminapp/users.html', content)

class UsersListView(UserPassesTestMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def test_func(self):
        return self.request.user.is_superuser


class UserCreatePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request):
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
        else:
            return render(request, 'adminapp/user_update.html', {'update_form': user_form})

    def get(self, request):
        title = 'пользователи / создание'
        user_form = ShopUserRegisterForm()
        content = {'title': title, 'update_form': user_form}
        return render(request, 'adminapp/user_update.html', content)


class UserUpdatePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        title = 'пользователи / редактирование'
        edit_user = get_object_or_404(ShopUser, pk=kwargs['pk'])
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
        else:
            content = {'title': title, 'update_form': edit_form}
            return render(request, 'adminapp/user_update.html', content)

    def get(self, request, **kwargs):
        title = 'пользователи / редактирование'
        edit_user = get_object_or_404(ShopUser, pk=kwargs['pk'])
        edit_form = ShopUserAdminEditForm(instance=edit_user)
        content = {'title': title, 'update_form': edit_form}
        return render(request, 'adminapp/user_update.html', content)


class UserDeletePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        user_item = get_object_or_404(ShopUser, pk=kwargs['pk'])
        # user_item.delete()
        if user_item.is_active:
            user_item.is_active = False
        else:
            user_item.is_active = True
        user_item.save()
        return HttpResponseRedirect(reverse('adminapp:users'))

    def get(self, request, **kwargs):
        title = 'пользователи / удаление'
        user_item = get_object_or_404(ShopUser, pk=kwargs['pk'])
        content = {'title': title, 'user_to_delete': user_item}
        return render(request, 'adminapp/user_delete.html', content)


class CategoriesPageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request):
        pass

    def get(self, request):
        title = 'админка / категории'
        categories_list = ProductCategory.objects.all()
        content = {
            'title': title,
            'objects': categories_list
        }
        return render(request, 'adminapp/categories.html', content)


class CategoryCreatePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request):
        category_form = ProductCategoryEditForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
        else:
            return render(request, 'adminapp/user_update.html', {'update_form': category_form})

    def get(self, request):
        title = 'категории / создание'
        category_form = ProductCategoryEditForm()
        content = {'title': title, 'update_form': category_form}
        return render(request, 'adminapp/category_update.html', content)


class CategoryUpdatePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        edit_category = get_object_or_404(ProductCategory, pk=kwargs['pk'])
        category_form = ProductCategoryEditForm(request.POST, instance=edit_category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
        else:
            return render(request, 'adminapp/user_update.html', {'update_form': category_form})

    def get(self, request, **kwargs):
        title = 'категории / редактирование'
        edit_category = get_object_or_404(ProductCategory, pk=kwargs['pk'])
        category_form = ProductCategoryEditForm(instance=edit_category)
        content = {'title': title, 'update_form': category_form}
        return render(request, 'adminapp/category_update.html', content)


class CategoryDeletePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        category_item = get_object_or_404(ProductCategory, pk=kwargs['pk'])
        if category_item.is_active:
            category_item.is_active = False
        else:
            category_item.is_active = True
        category_item.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    def get(self, request, **kwargs):
        title = 'категории / удаление'
        category_item = get_object_or_404(ShopUser, pk=kwargs['pk'])
        content = {'title': title, 'category_to_delete': category_item}
        return render(request, 'adminapp/category_delete.html', content)


class ProductsPageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        title = 'админка / продукты'
        category_item = get_object_or_404(ProductCategory, pk=kwargs['pk'])
        products_list = Product.objects.filter(category=category_item)
        content = {
            'title': title,
            'category': category_item,
            'objects': products_list
        }
        return render(request, 'adminapp/products.html', content)


class ProductCreatePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        category = get_object_or_404(ProductCategory, pk=kwargs['pk'])
        edit_form = ProductEditForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:products', kwargs={'pk': category.pk}))

    def get(self, request, **kwargs):
        title = 'продукт / добавить'
        category = get_object_or_404(ProductCategory, pk=kwargs['pk'])
        edit_form = ProductEditForm()
        content = {
            'title': title,
            'update_form': edit_form,
            'category': category
        }
        return render(request, 'adminapp/product_update.html', content)


class ProductReadPageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        title = 'продукт / подробнее'
        product = get_object_or_404(Product, pk=kwargs['pk'])
        content = {
            'title': title,
            'object': product
        }
        return render(request, 'adminapp/product_read.html', content)


class ProductUpdatePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        title = 'продукт / редактировать'
        edit_product = get_object_or_404(Product, pk=kwargs['pk'])
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:product_update', kwargs={'pk': edit_product.pk}))

    def get(self, request, **kwargs):
        title = 'продукт / редактировать'
        edit_product = get_object_or_404(Product, pk=kwargs['pk'])
        edit_form = ProductEditForm(instance=edit_product)
        content = {
            'title':  title,
            'update_form': edit_form,
            'category': edit_product.category
        }
        return render(request, 'adminapp/product_update.html', content)


class ProductDeletePageView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        if product.is_active:
            product.is_active = False
        else:
            product.is_active = True
        product.save()
        return HttpResponseRedirect(reverse('adminapp:products', kwargs={'pk': product.category.pk}))

    def get(self, request, **kwargs):
        title = 'продукт / удаление'
        product = get_object_or_404(Product, pk=kwargs['pk'])
        content = {'title': title, 'product_to_delete': product}
        return render(request, 'adminapp/product_delete.html', content)
