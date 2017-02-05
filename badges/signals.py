from django.dispatch import receiver
from django.db.models.signals import post_save

from models import Model3d
from utils import create_badge
from conf import BADGES_DICT


@receiver(post_save, sender=Model3d, dispatch_uid="set_collector")
def set_collector(sender, instance, **kwargs):
    model_count = Model3d.objects.filter(user=instance.user).count()
    if model_count is 5:
        create_badge(BADGES_DICT["Collector"], instance.user)


@receiver(post_save, sender=Model3d, dispatch_uid="set_star")
def set_star(sender, instance, **kwargs):
    if instance.views is 1000:
        create_badge(BADGES_DICT["Star"], instance.user)
