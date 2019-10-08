from Posts.views import posts_view
from django.conf.urls import url

urlpatterns = [
    url('feed', posts_view)
]