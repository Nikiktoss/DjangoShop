from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from authapp.models import ShopUser


def check_admin(user):
    return user.is_superuser


@user_passes_test(check_admin)
def main_admin(request):
    users = ShopUser.objects.all()
    return render(request, 'main_admin_page.html', context={'user': request.user, 'users': users})
