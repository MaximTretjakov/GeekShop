from django.contrib import admin
from .models import ShopUser


class ShopUserAdmin(admin.ModelAdmin):
    list_display = ('avatar', 'age')
    ordering = ['age']


admin.site.register(ShopUser, ShopUserAdmin)
