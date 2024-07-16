from rest_framework import mixins, status, viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from core.models import Point, Visit
from .serializers import (PointSerializer, VisitCreateSerializer,
                          VisitReadSerializer)


class PointRetrieveViewSet(mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

    def list(self, request, *args, **kwargs):
        queryset = request.user.my_points.all()
        if not queryset.exists():
            raise NotFound('Точки для данного сотрудника не найдены.')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class VisitCreateViewSet(mixins.CreateModelMixin,
                         viewsets.GenericViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitCreateSerializer

    def create(self, request, *args, **kwargs):
        """Переопределям ответ с полным набором полей."""
        serializer = self.get_serializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        response_serializer = VisitReadSerializer(
            serializer.instance, context={'request': request})
        return Response(response_serializer.data,
                        status=status.HTTP_201_CREATED, headers=headers)
