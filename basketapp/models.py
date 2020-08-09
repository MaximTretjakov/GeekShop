from django.conf import settings
from django.db import models
from django.db.models import Sum, F

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    add_date_time = models.DateField(auto_now_add=True, verbose_name='время')

    @staticmethod
    def total_amount():
        return Basket.objects.aggregate(Sum('quantity'))

    @staticmethod
    def value_of_goods():
        return Basket.objects.all().aggregate(
            total_summ=Sum(F('quantity') * F('product__price'), output_field=models.FloatField())
        )
