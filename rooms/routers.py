from rest_framework.routers import DefaultRouter
from rooms.views import RoomViewSet

router = DefaultRouter()

router.register( r'rooms', RoomViewSet)

urlpatterns = router.urls