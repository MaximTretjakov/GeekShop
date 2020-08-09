from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from basketapp.models import Basket
from .models import ProductCategory, Product


def get_basket(user):
    if user.is_authenticated:
        # return Basket.objects.filter(user=user)
        basket_data = {
            'total_amount': Basket.total_amount(),
            'value_of_goods': Basket.value_of_goods()
        }
        return basket_data
    else:
        return []


class HomePageView(View):
    def get(self, request):
        products = Product.objects.all()[:4]
        content = {
            'title': 'Магазин',
            'products': products,
            'basket': get_basket(request.user)
        }
        return render(request, 'mainapp/index.html', content)


class ContactPageView(View):
    def get(self, request):
        return render(request, 'mainapp/contact.html', {'title': 'Контакты', 'basket': get_basket(request.user)})


class ProductsPageView(View):
    def get(self, request, **kwargs):
        title = 'Продукты'
        category_menu = ProductCategory.objects.all()
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

        same_products = Product.objects.all()[:3]
        content = {
            'title': title,
            'category_menu': category_menu,
            'same_products': same_products,
            'basket': get_basket(request.user)
        }
        return render(request, 'mainapp/products.html', content)
