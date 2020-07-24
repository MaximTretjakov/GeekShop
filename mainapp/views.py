from django.shortcuts import render
from django.views.generic import View


class HomePageView(View):
    def get(self, request):
        return render(request, 'mainapp/index.html')


class ContactPageView(View):
    def get(self, request):
        return render(request, 'mainapp/contact.html')


class ProductsPageView(View):
    def get(self, request):
        return render(request, 'mainapp/products.html')
