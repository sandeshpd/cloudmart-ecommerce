from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core import views

handler404 = views.error_404
handler500 = views.error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('addresses/', include('addresses.urls')),
    path('inventory/', include('inventory.urls')),
]


# if settings.DEBUG is False:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)