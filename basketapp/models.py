from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    add_date_time = models.DateField(auto_now_add=True, verbose_name='время')

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = self.get_items_cached
        return sum(list(map(lambda x: x.quantity, items)))

    @property
    def total_cost(self):
        items = self.get_items_cached
        return sum(list(map(lambda x: x.product_cost, items)))

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by("product__category")

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()

    @cached_property
    def get_items_cached(self):
        return self.user.basket.select_related()
