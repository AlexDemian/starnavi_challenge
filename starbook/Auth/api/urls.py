from rest_framework.routers import DefaultRouter
from Auth.api.viewsets import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, 'auth')
urlpatterns = router.urls