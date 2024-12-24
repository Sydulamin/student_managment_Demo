from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, address


@receiver(post_save, sender=CustomUser)
def create_address(sender, instance, created, **kwargs):
    if created:
        address.objects.create(user=instance)
