from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
import json
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)


class DataMixin:
    def get_product_categories(self):
        return [
            {'href': 'mainapp:products_all', 'name': 'все', 'reverse_url': 'products_all'},
            {'href': 'mainapp:products_house', 'name': 'дом', 'reverse_url': 'products_house'},
            {'href': 'mainapp:products_office', 'name': 'офис', 'reverse_url': 'products_office'},
            {'href': 'mainapp:products_modern', 'name': 'модерн', 'reverse_url': 'products_modern'},
            {'href': 'mainapp:products_classic', 'name': 'классика', 'reverse_url': 'products_classic'},
        ]


class HomePageView(View):
    def get_dynamic_data(self):
        try:
            file_path = settings.BASE_DIR + '\\mainapp\\dynamic_data.json'
            with open(file_path, 'r', encoding="UTF-8") as f:
                return json.load(f)
        except Exception as e:
            logging.debug(e)

    def get(self, request):
        return render(request, 'mainapp/index.html', {'title': 'Магазин', 'dynamic_data': self.get_dynamic_data()})


class ContactPageView(View):
    def get(self, request):
        return render(request, 'mainapp/contact.html', {'title': 'Контакты'})


class ProductsPageView(DataMixin, View):
    def get(self, request):
        return render(
            request, 'mainapp/products.html', {'title': 'Продукты', 'links_menu': super().get_product_categories()}
        )


class ProductsPageAllView(DataMixin, View):
    def get(self, request):
        return render(
            request, 'mainapp/products.html',
            {'title': 'Продукты все', 'links_menu': super().get_product_categories()}
        )


class ProductsPageHomeView(DataMixin, View):
    def get(self, request):
        return render(
            request, 'mainapp/products.html',
            {'title': 'Продукты для дома', 'links_menu': super().get_product_categories()}
        )


class ProductsPageOfficeView(DataMixin, View):
    def get(self, request):
        return render(
            request, 'mainapp/products.html',
            {'title': 'Продукты для офиса', 'links_menu': super().get_product_categories()}
        )


class ProductsPageModernView(DataMixin, View):
    def get(self, request):
        return render(
            request, 'mainapp/products.html',
            {'title': 'Продукты модерн', 'links_menu': super().get_product_categories()}
        )


class ProductsPageClassicView(DataMixin, View):
    def get(self, request):
        return render(
            request, 'mainapp/products.html',
            {'title': 'Продукты классика', 'links_menu': super().get_product_categories()}
        )
