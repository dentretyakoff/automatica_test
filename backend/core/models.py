from django.db import models

from .validators import validate_phone_number


class Employee(models.Model):
    """Сотрудник."""
    name = models.CharField('ФИО сотрудника', max_length=255)
    phone = models.CharField(
        'Телефон',
        max_length=255,
        validators=(validate_phone_number,)
    )

    def __str__(self):
        return self.name

    @property
    def is_authenticated(self):
        return isinstance(self, Employee)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'phone'],
                                    name='unique_employee')
        ]


class Point(models.Model):
    """Торговая точка."""
    name = models.CharField('Название точки', max_length=255, unique=True)
    employee = models.ForeignKey(
        Employee,
        related_name='my_points',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Visit(models.Model):
    """Посещение торговых точек сотрудниками."""
    date = models.DateTimeField('Дата посещения', auto_now_add=True)
    point = models.ForeignKey(
        Point,
        related_name='visits',
        on_delete=models.CASCADE
    )
    employee = models.ForeignKey(
        Employee,
        related_name='my_visits',
        on_delete=models.CASCADE
    )
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    def __str__(self):
        return f'{self.date}: {self.point} - {self.employee}'
