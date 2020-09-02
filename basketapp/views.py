from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.template.loader import render_to_string

from basketapp.models import Basket
from mainapp.models import Product


class BasketAddPageView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def get(self, request, **kwargs):
        if 'login' in request.META.get('HTTP_REFERER'):
            return HttpResponseRedirect(reverse('mainapp:product_page', kwargs={'pk': kwargs['pk']}))
        product = get_object_or_404(Product, pk=kwargs['pk'])
        basket_item = Basket.objects.filter(product=product, user=request.user).first()
        if not basket_item:
            basket_item = Basket(product=product, user=request.user)

        basket_item.quantity += 1
        basket_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class BasketHomePageView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def get(self, request):
        title = 'Корзина'
        basket_items = Basket.objects.filter(user=request.user)
        content = {
            'title': title,
            'basket_items': basket_items
        }
        return render(request, 'basketapp/basket.html', content)


class BasketRemovePageView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def get(self, request, **kwargs):
        basket_record = get_object_or_404(Basket, pk=kwargs['pk'])
        basket_record.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class BasketEditPageView(LoginRequiredMixin, View):
    login_url = '/auth/login/'

    def get(self, request, **kwargs):
        if request.is_ajax():
            quantity = int(kwargs['quantity'])
            basket_item = Basket.objects.get(pk=kwargs['pk'])
            if quantity > 0:
                basket_item.quantity = quantity
                basket_item.save()
            else:
                basket_item.delete()

            basket_items = Basket.objects.filter(user=request.user)
            content = {
                'basket_items': basket_items,
            }
            result = render_to_string('basketapp/include/inc_basket_list.html', content)
            return JsonResponse({'result': result})
