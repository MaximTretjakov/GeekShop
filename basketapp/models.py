from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    add_date_time = models.DateField(auto_now_add=True, verbose_name='время')

    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.quantity, items)))

    @property
    def total_cost(self):
        items = Basket.objects.filter(user=self.user)
        return sum(list(map(lambda x: x.product_cost, items)))

    @staticmethod
    def get_items(user):
        return Basket.objects.filter(user=user).order_by("product__category")

    @staticmethod
    def get_item(pk):
        return Basket.objects.filter(pk=pk).first()
