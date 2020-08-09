from django.contrib import admin
from .models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'add_date_time')
    ordering = ['user']


admin.site.register(Basket, BasketAdmin)
