import random
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from basketapp.models import Basket
from .models import ProductCategory, Product


def get_hot_product():
    products_list = Product.objects.filter(category__is_active=True)
    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    return Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


class HomePageView(View):
    def get(self, request):
        products = Product.objects.filter(category__is_active=True)[:4]
        content = {
            'title': 'Магазин',
            'products': products,
            'basket': get_basket(request.user)
        }
        return render(request, 'mainapp/index.html', content)


class ContactPageView(View):
    def get(self, request):
        return render(request, 'mainapp/contact.html', {'title': 'Контакты', 'basket': get_basket(request.user)})


class ProductPageView(View):
    def get(self, request, **kwargs):
        title = 'продукты'
        product = get_object_or_404(Product, pk=kwargs['pk'])
        category_menu = ProductCategory.objects.all()
        content = {
            'title': title,
            'category_menu': category_menu,
            'product': product,
            'basket': get_basket(request.user),
        }
        return render(request, 'mainapp/product.html', content)


class ProductsPageView(View):
    def get(self, request, **kwargs):
        title = 'Продукты'
        category_menu = ProductCategory.objects.filter(is_active=True)
        pk = kwargs.get('pk', None)

        if pk is not None:
            if pk == 0:
                products_list = Product.objects.all()
                category = {'name': 'Все'}
            else:
                category = get_object_or_404(ProductCategory, pk=pk)
                products_list = Product.objects.filter(category__pk=pk)
            content = {
                'title': title,
                'category_menu': category_menu,
                'category': category,
                'products': products_list,
                'basket': get_basket(request.user)
            }
            return render(request, 'mainapp/products_list.html', content)

        hot_product = get_hot_product()
        same_products = get_same_products(hot_product)
        content = {
            'title': title,
            'category_menu': category_menu,
            'same_products': same_products,
            'basket': get_basket(request.user),
            'hot_product': hot_product
        }
        return render(request, 'mainapp/products.html', content)
