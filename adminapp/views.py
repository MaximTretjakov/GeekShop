from django.shortcuts import render
from django.views.generic import View

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class UsersPageView(View):
    def post(self, request):
        pass

    def get(self, request):
        title = 'админка / пользователи'
        users_list = ShopUser.objects.all()
        content = {
            'title': title,
            'objects': users_list
        }
        return render(request, 'adminapp/users.html', content)


class UserCreatePageView(View):
    def post(self, request):
        pass

    def get(self, request):
        pass


class UserUpdatePageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        pass


class UserDeletePageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        pass


class CategoriesPageView(View):
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


class CategoryCreatePageView(View):
    def post(self, request):
        pass

    def get(self, request):
        pass


class CategoryUpdatePageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        pass


class CategoryDeletePageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        pass


class ProductsPageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        title = 'админка / продукты'
        products_list = Product.objects.all()
        content = {
            'title': title,
            'objects': products_list
        }
        return render(request, 'adminapp/products.html', content)


class ProductCreatePageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        pass


class ProductReadPageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request):
        pass


class ProductUpdatePageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        pass


class ProductDeletePageView(View):
    def post(self, request, **kwargs):
        pass

    def get(self, request, **kwargs):
        pass
