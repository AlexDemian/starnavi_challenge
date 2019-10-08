from django.contrib.contenttypes.models import ContentType
from Events.models import Like


def make_like(instance, user):
    instance_type = ContentType.objects.get_for_model(instance)

    try:
        Like.objects.get(content_type=instance_type, object_id=instance.id, user=user).delete()
        return None

    except Like.DoesNotExist:
        like = Like.objects.create(content_type=instance_type, object_id=instance.id, user=user)
        return like
