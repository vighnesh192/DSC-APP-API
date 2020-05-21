from rest_framework import routers
from users.api import UsersViewSets

router = routers.DefaultRouter()
router.register('users', UsersViewSets, 'users')

urlpatterns = router.urls