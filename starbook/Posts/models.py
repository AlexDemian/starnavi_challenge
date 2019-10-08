from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User
from Events.models import Like


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True)
    body = models.TextField()
    likes = GenericRelation(Like)

    class Meta:
        db_table = 'posts'

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def liked_by_users(self):
        return list(self.likes.values_list('user_id', flat=True))


