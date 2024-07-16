from api.views import PointRetrieveViewSet, VisitCreateViewSet
from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('points', PointRetrieveViewSet)
router.register('visit', VisitCreateViewSet)

urlpatterns = [
    path(f'{settings.API_VERSION}/', include(router.urls)),
]
