from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='authapp')),
    path('basket/', include('basketapp.urls', namespace='basketapp')),
    path('admin/', include('adminapp.urls', namespace='adminapp')),
    path('order/', include('ordersapp.urls', namespace='order')),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
