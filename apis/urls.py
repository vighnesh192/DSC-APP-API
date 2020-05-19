from rest_framework import routers
from .api import ApisViewSets

router = routers.DefaultRouter()
router.register('api', ApisViewSets, 'api')

urlpatterns = router.urls