from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product


class BasketAddPageView(View):
    def get(self, request, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        basket_item = Basket.objects.filter(product=product, user=request.user).first()
        if not basket_item:
            basket_item = Basket(product=product, user=request.user)

        basket_item.quantity += 1
        basket_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class BasketHomePageView(View):
    def get(self, request):
        title = 'Корзина'
        content = {
            'title': title
        }
        return render(request, 'basketapp/basket.html', content)


class BasketRemovePageView(View):
    def get(self, request):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
