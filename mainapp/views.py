from django.shortcuts import render
from django.views.generic import View

from .models import ProductCategory, Product


class HomePageView(View):
    def get(self, request):
        products = Product.objects.all()[:4]
        content = {'title': 'Магазин', 'products': products}
        return render(request, 'mainapp/index.html', content)


class ContactPageView(View):
    def get(self, request):
        return render(request, 'mainapp/contact.html', {'title': 'Контакты'})


class ProductsPageView(View):
    def get(self, request, **kwargs):
        title = 'Продукты'
        if kwargs.get('pk', None):
            category = ProductCategory.objects.get(pk=kwargs['pk'])
            title = category.name
        same_products = Product.objects.all()[:3]
        category_menu = ProductCategory.objects.all()
        content = {'title': title, 'category_menu': category_menu, 'same_products': same_products}
        return render(request, 'mainapp/products.html', content)
