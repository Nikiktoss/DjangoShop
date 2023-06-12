from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import main_admin


urlpatterns = [
    path('', main_admin, name='admin_main_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
