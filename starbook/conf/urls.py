from django.conf.urls import include, url
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('api/events/', include('Events.api.urls'), name='api_events'),
    path('api/auth', include('Auth.api.urls'), name='auth'),
    path('api/posts', include('Posts.api.urls'), name='api_posts'),
    path('posts', include('Posts.urls'), name='posts'),
    path('api/token/get', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
