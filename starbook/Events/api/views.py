from rest_framework import viewsets
from Events.services import make_like
from Posts.models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def like_post(request):
    if not request.data.get('id'):
        return Response({"details": "Required argument 'id'"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        post = Post.objects.get(id=request.data['id'])
    except Post.DoesNotExist:
        return Response({"details": 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    make_like(post, request.user)
    return Response({"details": "Post %s (un)liked successfully" % post.id}, status=status.HTTP_201_CREATED)



