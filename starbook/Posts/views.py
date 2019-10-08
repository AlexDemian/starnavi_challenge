from django.shortcuts import render
from Posts.models import Post
import json

def posts_view(request):
    return render(request, 'Posts/main.html')
