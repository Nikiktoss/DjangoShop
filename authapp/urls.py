from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import shop_user_login, shop_user_logout, shop_user_register

urlpatterns = [
    path('login', shop_user_login, name='login_page'),
    path('logout', shop_user_logout, name='logout_page'),
    path('register', shop_user_register, name='registration_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
