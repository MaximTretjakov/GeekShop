import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import View
from django.conf import settings
from django.core.cache import cache

from .models import ProductCategory, Product


def get_hot_product():
    products_list = Product.objects.filter(category__is_active=True)
    return random.sample(list(products_list), 1)[0]


def get_same_products(hot_product):
    return Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]


class HomePageView(View):
    def get(self, request):
        # products = Product.objects.filter(category__is_active=True)[:4]
        products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:3]
        content = {
            'title': 'Магазин',
            'products': products,
        }
        return render(request, 'mainapp/index.html', content)


class ContactPageView(View):
    def get(self, request):
        return render(request, 'mainapp/contact.html', {'title': 'Контакты'})


@method_decorator(never_cache, name='dispatch')
class ProductPageView(View):
    def get(self, request, **kwargs):
        title = 'продукты'
        product = get_object_or_404(Product, pk=kwargs['pk'])
        category_menu = ProductCategory.objects.all()
        content = {
            'title': title,
            'category_menu': category_menu,
            'product': product,
        }
        return render(request, 'mainapp/product.html', content)


@method_decorator(never_cache, name='dispatch')
class ProductsPageView(View):
    def get(self, request, **kwargs):
        title = 'Продукты'
        category_menu = ProductCategory.objects.filter(is_active=True)
        pk = kwargs.get('pk', None)
        page = kwargs.get('page', 1)

        if pk is not None:
            if pk == 0:
                products_list = Product.objects.all()
                category = {'pk': 0, 'name': 'Все'}
            else:
                category = get_object_or_404(ProductCategory, pk=pk)
                products_list = Product.objects.filter(category__pk=pk)

            paginator = Paginator(products_list, 1)
            try:
                product_paginator = paginator.page(page)
            except PageNotAnInteger:
                product_paginator = paginator.page(1)
            except EmptyPage:
                product_paginator = paginator.page(paginator.num_pages)

            content = {
                'title': title,
                'category_menu': category_menu,
                'category': category,
                'products': product_paginator,
            }
            return render(request, 'mainapp/products_list.html', content)

        hot_product = get_hot_product()
        same_products = get_same_products(hot_product)
        content = {
            'title': title,
            'category_menu': category_menu,
            'same_products': same_products,
            'hot_product': hot_product
        }
        return render(request, 'mainapp/products.html', content)


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(
                category__pk=pk, is_active=True, category__is_active=True
            ).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(
            category__pk=pk, is_active=True, category__is_active=True
        ).order_by('price')


def products_ajax(request, pk=None, page=1):
    if request.is_ajax():
        links_menu = get_links_menu()

        if pk:
            if pk == '0':
                category = {
                    'pk': 0,
                    'name': 'все'
                }
                products = get_products_orederd_by_price()
            else:
                category = get_category(pk)
                products = get_products_in_category_orederd_by_price(pk)

            paginator = Paginator(products, 2)
            try:
                products_paginator = paginator.page(page)
            except PageNotAnInteger:
                products_paginator = paginator.page(1)
            except EmptyPage:
                products_paginator = paginator.page(paginator.num_pages)

            content = {
                'links_menu': links_menu,
                'category': category,
                'products': products_paginator,
            }

            result = render_to_string(
                'mainapp/includes/inc_products_list_content.html',
                context=content,
                request=request
            )

            return JsonResponse({'result': result})
