from django.contrib import admin

from .models import Employee, Point, Visit


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name',)


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee')
    search_fields = ('name',)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('date', 'point', 'employee', 'latitude', 'longitude')
    search_fields = ('point__name', 'employee__name',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
