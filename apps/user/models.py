from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(
        upload_to='users', blank=True, default='users/default.jpg')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    cover = models.ImageField(
        upload_to='users', null=True, blank=True)
    organization = models.OneToOneField(
        'partners.Organization', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self) -> str:
        return f'Профиль {self.user}'


@receiver(post_save, sender=User)
def send_order_confirmation_mail(sender: User, instance: User, created: bool, **kwargs):
    if created:
        Profile.objects.create(user=instance)
