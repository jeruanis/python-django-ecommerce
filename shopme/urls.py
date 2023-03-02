
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
import store


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('passage/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('currencies/', include('currencies.urls')),
    path('chatapp/', include('chatapp.urls')),
    path('customer/', include('customer.urls', namespace='customer')),
    path('seller/', views.seller_doc, name='seller_doc'),
    path('services/', views.services_doc, name='services_doc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #for media folder files access

