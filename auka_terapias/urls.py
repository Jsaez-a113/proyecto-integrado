"""
URL configuration for auka_terapias project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products import views as products_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls')),
]

# Handlers para páginas de error personalizadas
handler404 = products_views.custom_404
handler500 = products_views.custom_500
handler403 = products_views.custom_403
handler400 = products_views.custom_400

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Catch-all al final para capturar URLs no encontradas en desarrollo
    # Esto permite mostrar la página 404 personalizada incluso con DEBUG=True
    urlpatterns.append(path('<path:path>', products_views.custom_404))

