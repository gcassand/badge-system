from models import Badge


def create_badge(badge, user):
    """
    Create badge if doesn't exists then add the user to the M2M field.
    """
    badge, created = Badge.objects.get_or_create(
        name=badge["name"],
        description=badge["description"],
    )
    if created:
        badge.save()
    if not Badge.objects.filter(user=user).exists():
        badge.user.add(user)
        badge.save()
