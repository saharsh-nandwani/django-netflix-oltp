from rest_framework.routers import SimpleRouter
from .views import  NetflixViewSet

router= SimpleRouter()
router.register("netflix",NetflixViewSet)
urlpatterns = router.urls
