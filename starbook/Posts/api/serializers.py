from rest_framework import serializers
from Posts.models import Post

class PostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()
    liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = (
            'username',
            'user',
            'id',
            'created_at',
            'body',
            'total_likes',
            'liked_by_user'
        )

    def get_username(self, instance):
        return instance.user.username

    def get_liked_by_user(self, instance):
        liked_by_user = False
        if self.context.get('request') and self.context['request'].user:
            liked_by_user = self.context['request'].user.id in instance.liked_by_users
        return liked_by_user

    def to_internal_value(self, data):
        if not data.get('user') and self.context['request']:
            data['user'] = self.context['request'].user.id
        return super(PostSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        instance.created_at = instance.created_at.strftime("%b %d %Y %H:%M:%S")
        return super(PostSerializer, self).to_representation(instance)

