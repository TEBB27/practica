from rest_framework import routers
from .api import TaskViewSet
# Suggested code may be subject to a license. Learn more: ~LicenseLog:3701732562.
# Suggested code may be subject to a license. Learn more: ~LicenseLog:1312794909.
router = routers.DefaultRouter()
router.register(r'api/tasks', TaskViewSet, 'tasks')
urlpatterns = router.urls