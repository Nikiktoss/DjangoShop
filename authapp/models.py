from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class ShopUser(AbstractUser):
    photo = models.ImageField(upload_to='users_photo', verbose_name="Account photo", blank=True)
    age = models.PositiveIntegerField(verbose_name="Age", default=18)


class ShopUserProfile(models.Model):
    MALE = "M"
    FEMALE = "W"

    gender_choices = ((MALE, "M"), (FEMALE, "W"))

    user = models.OneToOneField(ShopUser, verbose_name="User", null=False, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, verbose_name="Gender", choices=gender_choices, blank=True)
    about_me = models.TextField(verbose_name="About me", max_length=512, blank=True)

    @staticmethod
    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @staticmethod
    @receiver(post_save, sender=ShopUser)
    def save_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
