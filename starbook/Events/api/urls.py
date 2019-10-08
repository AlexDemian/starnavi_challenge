from django.conf.urls import url
from Events.api.views import like_post

urlpatterns = [
    url('like/post', like_post)
]
