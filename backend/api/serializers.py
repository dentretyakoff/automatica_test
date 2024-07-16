from core.models import Point, Visit
from rest_framework import serializers


class PointSerializer(serializers.ModelSerializer):
    """Сериализатор торговых точек."""

    class Meta:
        model = Point
        fields = ('id', 'name')


class VisitReadSerializer(serializers.ModelSerializer):
    """Сериализатор чтения посещений."""

    class Meta:
        model = Visit
        fields = ('id', 'date')


class VisitCreateSerializer(serializers.ModelSerializer):
    """Сериализатор создания посещений."""
    id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    class Meta:
        model = Visit
        fields = ('id', 'latitude', 'longitude')

    def validate(self, attrs):
        user = self.context['request'].user
        point_id = attrs['id']
        try:
            point = Point.objects.get(pk=point_id)
        except Point.DoesNotExist:
            raise serializers.ValidationError(
                f'Точка с id {point_id} не существует.')
        if user != point.employee:
            raise serializers.ValidationError(
                'Сотрудник не привязан к указанной точке')
        attrs['point'] = point
        attrs['user'] = user

        return super().validate(attrs)

    def create(self, validated_data):
        return Visit.objects.create(
            employee=validated_data['user'],
            point=validated_data['point'],
            latitude=validated_data['latitude'],
            longitude=validated_data['longitude'])
