from rest_framework.routers import DefaultRouter
from Posts.api.viewsets import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet)
urlpatterns = router.urls

