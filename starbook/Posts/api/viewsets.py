from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Posts.models import Post
from Posts.api.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )